import pandas as pd
from etl.logger import logger

from etl.extract import extract_data
from etl.validate import validate_data
from etl.deduplicate import remove_duplicates
from etl.fraud_rules import apply_fraud_rules
from etl.transform import transform_data
from etl.load import load_data

from etl.paths import INTERMEDIATE_PATH

def extract_task():

    df = extract_data()
    output_file = (INTERMEDIATE_PATH / "extracted.pkl")
    df.to_pickle(output_file)

def validate_task():
    input_file = (INTERMEDIATE_PATH / "extracted.pkl")
    df = pd.read_pickle(input_file)
    df = validate_data(df)

    output_file = (INTERMEDIATE_PATH / "validated.pkl")

    df.to_pickle(output_file)

def deduplicate_task():
    input_file = (INTERMEDIATE_PATH / "validated.pkl")
    df = pd.read_pickle(input_file)
    df = remove_duplicates(df)
    
    output_file = (INTERMEDIATE_PATH / "deduplicated.pkl")

    df.to_pickle(output_file)

def fraud_task():

    input_file = (INTERMEDIATE_PATH/ "deduplicated.pkl")
    df = pd.read_pickle(input_file)
    df = apply_fraud_rules(df)

    output_file = (INTERMEDIATE_PATH/ "fraud.pkl")

    df.to_pickle(output_file)

def transform_task():

    input_file = (INTERMEDIATE_PATH/ "fraud.pkl")
    df = pd.read_pickle(input_file)
    df = transform_data(df)

    output_file = (INTERMEDIATE_PATH/ "transformed.pkl")

    df.to_pickle(output_file)

def load_task():

    input_file = (INTERMEDIATE_PATH/ "transformed.pkl")

    df = pd.read_pickle(input_file)

    load_data(df)

    #Cleanup intermediate files
    for file in INTERMEDIATE_PATH.glob("*.pkl"):
        try:
            file.unlink()
        except Exception as e:
            logger.error(f"Failed to delete {file}: {e}")

    logger.info("Intermediate files cleaned successfully")
