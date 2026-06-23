import pandas as pd

from datetime import datetime
from etl.logger import logger


def transform_data(df):

    logger.info("Starting transformation layer")

    #Ensure timestamp type
    df["transaction_timestamp"] = pd.to_datetime(
        df["transaction_timestamp"]
    )

    #Hour
    df["transaction_hour"] = (
        df["transaction_timestamp"].dt.hour
    )

    #Day Name
    df["transaction_day"] = (
        df["transaction_timestamp"].dt.day_name()
    )

    #Date
    df["transaction_date"] = (
        df["transaction_timestamp"].dt.date
    )

    #Amount Bucket
    def classify_amount(amount):

        if amount < 1000:
            return "LOW"
        elif amount < 10000:
            return "MEDIUM"
        elif amount < 100000:
            return "HIGH"
        return "VERY_HIGH"
    
    df["amount_bucket"] = (
        df["amount"].apply(classify_amount)
    )

    #Processing Timestamp
    df["processing_timestamp"] = (
        datetime.now()
    )

    #Risk Category
    def risk_category(score):

        if score == 0:
            return "LOW"
        elif score <= 30:
            return "MEDIUM"
        elif score <= 60:
            return "HIGH"
        return "CRITICAL"

    df["risk_category"] = (
        df["fraud_score"].apply(risk_category)
    )

    logger.info("Transformation completed")

    return df






