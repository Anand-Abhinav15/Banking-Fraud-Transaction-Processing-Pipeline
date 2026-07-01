from faker import Faker
import pandas as pd
import random
import uuid
from pathlib import Path
from datetime import datetime, timedelta

fake = Faker()

NUM_RECORDS = 100000

payment_channels = [
    "ATM",
    "MOBILE",
    "POS",
    "ONLINE"
]

transaction_types = [
    "DEBIT",
    "CREDIT",
    "TRANSFER"
]

currencies = [
    "INR",
    "USD",
    "EUR"
]

locations = [
    "Mumbai",
    "Delhi",
    "Bangalore",
    "Chennai",
    "Pune",
    "Hyderabad",
    "Kolkata"
]

records = []

start_date = datetime(2026, 1, 1)

for i in range(NUM_RECORDS):

    amount = round(
        random.uniform(100, 200000),
        2
    )

    txn_time = (
        start_date
        + timedelta(
            minutes=random.randint(
                0,
                180 * 24 * 60
            )
        )
    )

    record = {
        "transaction_id":
            f"TXN{uuid.uuid4().hex[:12]}",

        "customer_id":
            f"CUST{random.randint(1,5000):05}",

        "account_number":
            f"ACC{random.randint(10000000,99999999)}",

        "transaction_type":
            random.choice(transaction_types),

        "merchant_id":
            f"M{random.randint(1000,9999)}",

        "amount":
            amount,

        "currency":
            random.choice(currencies),

        "transaction_timestamp":
            txn_time,

        "device_id":
            f"D{random.randint(1000,9999)}",

        "location":
            random.choice(locations),

        "payment_channel":
            random.choice(payment_channels),

        "status":
            "SUCCESS"
    }

    records.append(record)

df = pd.DataFrame(records)

Path("data/raw").mkdir(
    parents=True,
    exist_ok=True
)

df.to_csv(
    "data/raw/transactions_2026_large.csv",
    index=False
)

print(
    f"{len(df)} records generated."
)