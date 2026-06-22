import pandas as pd

from etl.logger import logger
from etl.config_loader import load_config

def apply_fraud_rules(df):

    logger.info("Starting fraud detection")

    cofig = load_config()

    high_amount_threshold = (
        config["fraud_rules"]
        ["high_amount_threshold"]
    )

    rapid_txn_limit = (
        config["fraud_rules"]
        ["rapid_txn_limit"]
    )

    fraud_flags = []
    fraud_scores = []

    df["transaction_timestamp"] = pd.to_datetime(
        df["transaction_timestamp"]
    )

    ## Rapid Trasaction Detection

    rapid_customers = []

    customer_counts = (
        df.groupby("customer_id").size()
    )

    rapid_customers = customer_counts[
        customer_counts > rapid_txn_limit
    ].index.tolist()

    ## Process Each Transaction

    for _, row in df.iterrows():
        
        flags = []

        score = 0

        #High Amount
        if row["amount"] > high_amount_threshold:

            flags.append("HIGH_AMOUNT")

            score += 40

        #Night Transaction
        hour = (
            row["transaction_timestamp"].hour
        )

        if 1 <= hour < 4:

            flags.append("NIGHT_TRANSACTION")

            score += 20

        # Rapid Transaction
        if row["customer_id"] in rapid_customers:

            flags.append("RAPID_TRANSACTION")

            score += 30

        fraud_flags.append(
            ",".join(flags)
        )

        fraud_scores.append(score)

    df["fraud_flag"] = fraud_flags

    df["fraud_score"] = fraud_scores

    logger.info("Fraud detection completed")

    return df
