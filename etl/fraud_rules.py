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

    ## Rapid Transaction Detection (Rolling Window)

    rapid_transaction_ids = set()

    for customer_id, group in df.groupby("customer_id"):

        group = group.sort_values(
            "transaction_timestamp"
        )

        timestamps = group["transaction_timestamp"]

        for idx, current_time in timestamps.items():

            window_start = (
                current_time
                - pd.Timedelta(minutes=2)
            )

            txn_count = (
                (
                    timestamps >= window_start
                )
                &
                (
                    timestamps <= current_time
                )
            ).sum()

            if txn_count > rapid_txn_limit:

                rapid_transaction_ids.add(idx)

    ## Geo Anamoly Detection

    geo_transaction_ids = set()

    for customer_id, group in df.groupby("customer_id"):

        group = group.sort_values(
            "transaction_timestamp"
        )

        for i in range(1, len(group)):

            current_row = group.iloc[i]

            previous_row = group.iloc[i - 1]

            time_diff = (
                current_row["transaction_timestamp"]
                - previous_row["transaction_timestamp"]
            )

            if (
                current_row["location"]
                != previous_row["location"]
                and time_diff.total_seconds()
                <= 600
            ):

                geo_transaction_ids.add(
                    current_row.name
                ) 


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
        if row.name in rapid_transaction_ids:

            flags.append("RAPID_TRANSACTION")

            score += 30

        
        # Geo Anomoly check
        if row.name in geo_transaction_ids:

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
