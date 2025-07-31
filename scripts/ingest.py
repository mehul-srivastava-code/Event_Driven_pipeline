import pandas as pd
import os
import glob

base_dir = r"C:\Users\mehul\OneDrive\Desktop\intership"
csv_source = os.path.join(base_dir, "source data", "input.csv")
json_folder = os.path.join(base_dir, "source data", "json_orders")
data_dir = os.path.join(base_dir, "data")


os.makedirs(data_dir, exist_ok=True)

csv_target = os.path.join(data_dir, "incoming.csv")
json_target = os.path.join(data_dir, "incoming_from_json.csv")

if os.path.exists(csv_source):
    try:
        df_csv = pd.read_csv(csv_source)
        if os.path.exists(csv_target):
            df_csv.to_csv(csv_target, mode="a", header=False, index=False)
        else:
            df_csv.to_csv(csv_target, index=False)
        print(f"CSV: Ingested {len(df_csv)} rows into {csv_target}")
    except Exception as e:
        print(f"WARNING: CSV ingestion failed: {e}")
else:
    print("INFO: No input.csv found, skipping CSV ingestion.")


if os.path.exists(json_folder):
    json_files = sorted(glob.glob(os.path.join(json_folder, "*.json")))
    all_data = []
    for file in json_files:
        try:
            df = pd.read_json(file)
            all_data.append(df)
            print(f"JSON: Loaded {file}")
        except Exception as e:
            print(f"WARNING: JSON: Failed to load {file}: {e}")

    if all_data:
        combined = pd.concat(all_data, ignore_index=True)
        if os.path.exists(json_target):
            combined.to_csv(json_target, mode="a", header=False, index=False)
        else:
            combined.to_csv(json_target, index=False)
        print(f"JSON: Ingested {len(combined)} rows into {json_target}")
    else:
        print("INFO: No valid JSON files found.")
else:
    print("INFO: JSON folder not found, skipping JSON ingestion.")
