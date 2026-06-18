from etl.extract import extract_data
from etl.validate import validate_data
from etl.deduplicate import remove_duplicates
from etl.fraud_rules import apply_fraud_rules
from etl.transform import transform_data
from etl.load import load_data

def run_pipeline():

    df = extract_data()

    df = validate_data()

    df = remove_duplicates()

    df = apply_fraud_rules()

    df = transform_data()

    load_data(df)


if __name__ == "__main__":
    run_pipeline()
    






