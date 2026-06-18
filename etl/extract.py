import pandas as pd
from pathlib import Path

from etl.logger import logger

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DATA_PATH = BASE_DIR / "data" / "raw"


def extract_data():

    logger.info("Starting extraction process")

    csv_files = list(RAW_DATA_PATH.glob("*.csv"))

    if not csv_files:
        raise FileNotFoundError(
            f"No CSV files found in {RAW_DATA_PATH}"
        )

    logger.info(f"Found {len(csv_files)} files")

    dataframes = []

    for file in csv_files:

        logger.info(f"Reading file: {file.name}")

        df = pd.read_csv(file)

        logger.info(
            f"{file.name} contains {len(df)} records"
        )

        dataframes.append(df)

    combined_df = pd.concat(
        dataframes,
        ignore_index=True
    )

    logger.info(
        f"Total records extracted: {len(combined_df)}"
    )

    return combined_df