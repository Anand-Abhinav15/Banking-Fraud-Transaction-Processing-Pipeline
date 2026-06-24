from sqlalchemy import create_engine
from dotenv import load_dotenv
from pathlib import Path

import os

from etl.logger import logger

load_dotenv()


def get_engine():

    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    host = os.getenv("POSTGRES_HOST")
    port = os.getenv("POSTGRES_PORT")
    db = os.getenv("POSTGRES_DB")

    connection_string = (
        f"postgresql://{user}:{password}"
        f"@{host}:{port}/{db}"
    )

    return create_engine(connection_string)


def load_to_postgres(df):

    logger.info("Loading data to PostgreSQL")

    engine = get_engine()

    df.to_sql(
        "clean_transactions", engine, if_exists = "append", index = False
    )

    logger.info(
        f"{len(df)} records loaded"
    )


def save_parquet_partitioned(df):

    logger.info("Saving parquet partitions")

    for date, group in df.groupby("transaction_date"):

        year = date.year
        month = str(date.month).zfill(2)
        day = str(date.day).zfill(2)

        partition_path = (
            f"data/pocessed/"
            f"year= {year}"
            f"month= {month}"
            f"day = {day}"
        )

        Path(partition_path).mkdir(parents= True, exists_ok = True)

        output_file = (
            f"{partition_path}/"
            f"transactions.parquet"
        )

        group.to_parquet(output_file, index=False)

    logger.info("Parquet storage completed")



def load_data(df):

    load_to_postgres(df)

    save_parquet_partitioned(df)

