import pandas as pd
from datetime import datetime

from etl.logger import logger
from etl.config_loader import load_config

from etl.paths import REJECTED_PATH

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
                    f"Missing {column}"
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

        
        ## Currency Validation

        if row["currency"] not in allowed_currencies:

            errors.append(
                "Invalid currency"
            )
            
        ## Timestamp validation

        try:

            pd.to_datetime(
                row["transaction_timestamp"]
            )

        except:
            
            errors.append(
                "Invalid timestamp"
            )

        ## Account Validation

        account = str(
            row["account_number"]
        )

        if not (
            account.startswith("ACC")
            and len(account) == 11
        ):
            
            errors.append(
                "Invalid account number"
            )

        ## Classification

        if errors:

            row_copy = row.copy()

            row_copy["rejection_reason"] = (
                " | ".join(errors)
            )

            rejected_records.append(
                row_copy
            )

        else:

            valid_records.append(row)

    valid_df = pd.DataFrame(valid_records)

    rejected_records = pd.DataFrame(
        rejected_records
    )

    logger.info(
        f"Valid records: {len(valid_df)}"
    )

    logger.info(
        f"Rejected records: {len(rejected_records)}"
    )

    rejected_records.to_csv(
        REJECTED_PATH / "rejected_transactions.csv",
        index = False
    )

    return valid_df