from sqlalchemy import create_engine
from dotenv import load_dotenv
from pathlib import Path
import uuid
import os

from etl.logger import logger
from etl.paths import PROCESSED_PATH

# Load .env.local only if it exists
env_path = Path(".env.local")

if env_path.exists():
    load_dotenv(env_path)


def get_engine():

    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    host = os.getenv("POSTGRES_HOST")
    port = os.getenv("POSTGRES_PORT")
    db = os.getenv("POSTGRES_DB")

    print(f"USER={user}")
    print(f"PASSWORD={password}")
    print(f"HOST={host}")
    print(f"PORT={port}")
    print(f"DB={db}")

    connection_string = (
        f"postgresql://{user}:{password}"
        f"@{host}:{port}/{db}"
    )

    print(connection_string)

    return create_engine(connection_string)


def load_to_postgres(df):

    logger.info("Loading data to PostgreSQL")

    engine = get_engine()

    temp_table = (
        f"temp_transactions_{uuid.uuid4().hex[:8]}"
    )

    df.to_sql(
        temp_table, engine, index = False, if_exists = "replace"
    )

    columns = list(df.columns)

    column_names = ", ".join(columns)

    updated_columns = ", ".join(
        [
            f"{col}= EXCLUDED.{col}"
            for col in columns
            if col != "transaction_id"
        ]
    )

    upsert_query = f"""
    INSERT INTO clean_transactions
    ({column_names})

    SELECT
    {column_names}
    FROM {temp_table}

    ON CONFLICT (transaction_id)
    DO UPDATE
    SET
    {updated_columns}
    """

    with engine.begin() as conn:

        conn.exec_driver_sql(upsert_query)

        conn.exec_driver_sql(
            f"DROP TABLE {temp_table}"
        )

    logger.info(
        f"{len(df)} records upserted"
    )


def save_parquet_partitioned(df):

    logger.info("Saving parquet partitions")

    for date, group in df.groupby("transaction_date"):

        year = date.year
        month = str(date.month).zfill(2)
        day = str(date.day).zfill(2)

        partition_path = (
            PROCESSED_PATH
            / f"year= {year}"
            / f"month= {month}"
            / f"day = {day}"
        )

        partition_path.mkdir(parents=True, exist_ok=True)

        output_file = (
            partition_path
            / "transactions.parquet"
        )

        group.to_parquet(output_file, index=False)

    logger.info("Parquet storage completed")



def load_data(df):

    load_to_postgres(df)

    save_parquet_partitioned(df)

