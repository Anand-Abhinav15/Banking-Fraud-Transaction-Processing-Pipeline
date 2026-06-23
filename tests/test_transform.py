from etl.extract import extract_data
from etl.validate import validate_data
from etl.deduplicate import remove_duplicates
from etl.fraud_rules import apply_fraud_rules
from etl.transform import transform_data


df = extract_data()

df = validate_data(df)

df = remove_duplicates(df)

df = apply_fraud_rules(df)

df = transform_data(df)

print(
    df[
        ["transaction_id", "amount", "amount_bucket", "fraud_score", "risk_category", "transaction_hour"]
    ]
)


