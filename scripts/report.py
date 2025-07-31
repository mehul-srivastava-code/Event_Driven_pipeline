import pandas as pd
import matplotlib.pyplot as plt
import os


base_dir = r"C:\Users\mehul\OneDrive\Desktop\intership"
processed_path = os.path.join(base_dir, "processed", "processed.csv")
report_csv = os.path.join(base_dir, "processed", "daily_report.csv")
report_png = os.path.join(base_dir, "processed", "daily_report.png")


if not os.path.exists(processed_path):
    print(f" File not found: {processed_path}")
    exit(1)


df = pd.read_csv(processed_path)
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df['Date'] = df['Timestamp'].dt.date


summary = df.groupby('Date').size().reset_index(name='Records')
summary.to_csv(report_csv, index=False)


plt.figure(figsize=(6, 4))
summary.plot(x='Date', y='Records', kind='bar', legend=False, title='Daily Records Count')
plt.tight_layout()
plt.savefig(report_png)

print(" Report generated successfully.")
