from etl.extract import extract_data

df = extract_data()

print(df.head())

print()
print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")
