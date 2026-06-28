import pandas as pd

from etl.logger import logger

from etl.paths import REJECTED_PATH

def remove_duplicates(df):

    logger.info("Starting deduplication process")

    #Convert timestamp first
    df["transaction_timestamp"] = pd.to_datetime(
        df["transaction_timestamp"]
    )

    duplicate_records = df[
        df.duplicated(
            subset = ["transaction_id"],
            keep = "last"
        )
    ]

    duplicate_records.to_csv(
        REJECTED_PATH / "duplicate_transaction.csv",
        index = False
    )

    duplicate_count = len(
        duplicate_records
    )

    deduplicated_df = df.drop_duplicates(
        subset= ["transaction_id"],
        keep= "last"
    )


    logger.info(f"Duplicate rows removed: {duplicate_count}")

    return deduplicated_df



