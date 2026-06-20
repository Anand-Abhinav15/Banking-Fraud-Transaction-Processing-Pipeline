from etl.extract import extract_data
from etl.validate import validate_data

df = extract_data()

valid_df = validate_data(df)

print()

print(
    f"Valid Records: {len(valid_df)}"
)





