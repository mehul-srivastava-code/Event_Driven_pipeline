import pandas as pd
import os

base_dir = os.getcwd()
csv_path = os.path.join(base_dir, "data", "incoming.csv")

if not os.path.exists(csv_path):
    print(f"ERROR: File not found: {csv_path}")
    exit(1)

df = pd.read_csv(csv_path, header=None, names=["First", "Last", "Timestamp"])
df['FullName'] = df['First'] + ' ' + df['Last']

processed_dir = os.path.join(base_dir, "processed")
os.makedirs(processed_dir, exist_ok=True)
df.to_csv(os.path.join(processed_dir, "processed.csv"), index=False)

print(f"Processed {len(df)} rows and saved to processed.csv")
