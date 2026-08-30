import pandas as pd
import os

# -----------------------------
# 1. Load raw dataset
# -----------------------------
input_file = "data/raw/household_power_consumption.txt"

df = pd.read_csv(
    input_file,
    sep=";",
    na_values="?",
    low_memory=False
)

print("Original shape:", df.shape)


# -----------------------------
# 2. Convert columns to numeric
# -----------------------------
numeric_columns = [
    "Global_active_power",
    "Global_reactive_power",
    "Voltage",
    "Global_intensity",
    "Sub_metering_1",
    "Sub_metering_2",
    "Sub_metering_3"
]

for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")


# -----------------------------
# 3. Create datetime
# -----------------------------
df["datetime"] = pd.to_datetime(
    df["Date"] + " " + df["Time"],
    dayfirst=True
)

# Remove rows with missing values
df = df.dropna(subset=["datetime", "Global_active_power"])

# Sort by datetime
df = df.sort_values("datetime")

print("Rows after cleaning:", len(df))


# -----------------------------
# 4. Set datetime as index
# -----------------------------
df = df.set_index("datetime")


# -----------------------------
# 5. Convert minute data to hourly data
# -----------------------------
hourly = df["Global_active_power"].resample("1h").mean()

hourly = hourly.dropna()

print("Hourly dataset shape:", hourly.shape)


# -----------------------------
# 6. Create features
# -----------------------------
result = pd.DataFrame()

result["hour"] = hourly.index.hour
result["day"] = hourly.index.day
result["month"] = hourly.index.month
result["day_of_week"] = hourly.index.dayofweek

# Weekend = 1, Weekday = 0
result["is_weekend"] = (
    result["day_of_week"] >= 5
).astype(int)

# Previous hour consumption
result["previous_consumption"] = hourly.shift(1).values

# Target
result["Global_active_power"] = hourly.values

# Remove first row
result = result.dropna()


# -----------------------------
# 7. Save processed dataset
# -----------------------------
os.makedirs("data/processed", exist_ok=True)

output_file = "data/processed/energy_processed.csv"

result.to_csv(output_file, index=False)

print("\nProcessed dataset saved to:")
print(output_file)

print("\nFinal dataset shape:", result.shape)

print("\nFirst 5 rows:")
print(result.head())