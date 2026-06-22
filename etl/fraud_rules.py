import pandas as pd

from etl.logger import logger
from etl.config_loader import load_config

def apply_fraud_rules(df):

    logger.info("Starting fraud detection")

    config = load_config()

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

    df["amount"] = df["amount"].astype(float)

    ## Rapid Trasaction Detection

    rapid_customers = []

    customer_counts = (
        df.groupby("customer_id").size()
    )

    rapid_customers = customer_counts[
        customer_counts > rapid_txn_limit
    ].index.tolist()

    #Geo Anamoly Detection

    geo_customers = []

    for customer_id, group in df.groupby("customer_id"):

        unique_locations = (
            group["location"].nunique()
        )

        if unique_locations >= 3:

            geo_customers.append(customer_id)


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

        
        # Geo Anomoly
        if row["customer_id"] in geo_customers:

            flags.append("GEO_ANOMALY")

            score += 30

        #save results
        fraud_flags.append(
            ",".join(flags)
        )

        fraud_scores.append(score)

        
    # Create Fraud Columns
    df["fraud_flag"] = fraud_flags

    df["fraud_score"] = fraud_scores

    df["is_high_risk"] = (df["fraud_score"] >= 50) 

    logger.info(
        f"Total Fraud Transactions: "
        f"{(df['fraud_score'] > 0).sum()}"
    )

    logger.info("Fraud detection completed")

    logger.info(
        f"High Risk Transaction: "
        f"{df['is_high_risk'].sum()}"
    )

    return df
