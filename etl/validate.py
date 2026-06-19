import pandas as pd
from datetime import datetime

from etl.logger import logger
from etl.config_loader import load_config

def validate_data(df):

    logger.info("Starting validation")

    config = load_config()

    allowed_currencies = (
        config["validation"]["allowed_currencies"]
    )

    mandatory_columns = (
        config["validation"]["mandatory_columns"]
    )

    valid_records = []
    rejected_records = []

    for _, row in df.iterrows():

        errors = []

        ## Mandatory Fields

        for column in mandatory_columns:

            if pd.isna(row[column]):

                errors.append(
                    f"Missing {columns}"
                )

        ## Amount Validation

        try:

            amount = float(row["amount"])

            if amount <= 0:

                errors.append(
                    "Negative amount"
                )

        except:
            
            errors.append(
                "Invalid amount"
            )

            

