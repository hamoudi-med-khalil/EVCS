# scripts/clean_and_aggregate_ev.py

import pandas as pd

# Load the dataset
df_ev = pd.read_csv("data/Electric_Vehicle_Charging_Station_Data.csv")

# Convert Start_Date___Time to datetime
df_ev['Start_Date___Time'] = pd.to_datetime(df_ev['Start_Date___Time'], errors='coerce')

# Drop duplicate rows
df_ev_cleaned = df_ev.drop_duplicates()

# Extract date only (without time) and group by date
df_ev_cleaned['date'] = df_ev_cleaned['Start_Date___Time'].dt.date
df_agg = df_ev_cleaned.groupby('date')['Energy__kWh_'].sum().reset_index()

# Rename columns for clarity
df_agg.columns = ['date', 'energy']

# Save to processed folder
df_agg.to_csv("data/processed/aggregated_ev_energy.csv", index=False)

print("[✅] Aggregation complete. Saved to data/processed/aggregated_ev_energy.csv")
