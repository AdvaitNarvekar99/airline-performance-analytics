import pandas as pd
import os

input_path = os.path.join("data", "Airline_Delay_Cause.csv")
output_path = os.path.join("outputs", "Cleaned_Airline_Delay.csv")

df = pd.read_csv(input_path)

df.columns = df.columns.str.strip().str.replace(" ", "_").str.lower()
df.dropna(subset=["year", "month", "airport", "carrier"], inplace=True)

df["year"] = df["year"].astype(int)
df["month"] = df["month"].astype(int)
df["arr_delay"] = pd.to_numeric(df["arr_delay"], errors="coerce")

df.to_csv(output_path, index=False)
print(f"✅ Cleaned CSV saved to: {output_path}")
