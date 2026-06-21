from etl.extract import extract_data
from etl.validate import validate_data
from etl.deduplicate import remove_duplicates

df = extract_data()

df = validate_data(df)

df = remove_duplicates(df)

print()

print(
    f"Final Record Count: {len(df)}"
)


