from etl.extract import extract_data
from etl.validate import validate_data
from etl.deduplicate import remove_duplicates
from etl.fraud_rules import apply_fraud_rules

df = extract_data()

df = validate_data(df)

df = remove_duplicates(df)

df = apply_fraud_rules(df)

print(
    df[
        ["transaction_id", "customer_id", "fraud_flag", "fraud_score", "is_high_risk"]
    ]
)


