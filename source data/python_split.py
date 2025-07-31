import pandas as pd
import os


file_path = r"C:\Users\mehul\OneDrive\Desktop\intership\source data\data.csv"
output_dir = r"C:\Users\mehul\OneDrive\Desktop\intership\source data\json_orders"

os.makedirs(output_dir, exist_ok=True)


df = pd.read_csv(file_path, encoding="ISO-8859-1")

chunk_size = 100
for i in range(0, len(df), chunk_size):
    chunk = df.iloc[i:i+chunk_size]
    output_file = os.path.join(output_dir, f"orders_{i//chunk_size + 1}.json")
    chunk.to_json(output_file, orient="records", lines=False)

print(f" JSON files written to: {output_dir}")
