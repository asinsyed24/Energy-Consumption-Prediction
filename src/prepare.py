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
# 3. Combine Date and Time
# -----------------------------
df["datetime"] = pd.to_datetime(
    df["Date"] + " " + df["Time"],
    dayfirst=True
)

# Sort by time
df = df.sort_values("datetime")


# -----------------------------
# 4. Remove missing values
# -----------------------------
df = df.dropna()

print("Shape after removing missing values:", df.shape)


# -----------------------------
# 5. Create time features
# -----------------------------
df["hour"] = df["datetime"].dt.hour
df["day"] = df["datetime"].dt.day
df["month"] = df["datetime"].dt.month
df["day_of_week"] = df["datetime"].dt.dayofweek

# 1 = weekend, 0 = weekday
df["is_weekend"] = (df["day_of_week"] >= 5).astype(int)


# -----------------------------
# 6. Create previous consumption
# -----------------------------
df["previous_consumption"] = df["Global_active_power"].shift(1)

# Remove first row because it has no previous value
df = df.dropna()


# -----------------------------
# 7. Select required columns
# -----------------------------
final_df = df[
    [
        "datetime",
        "hour",
        "day",
        "month",
        "day_of_week",
        "is_weekend",
        "previous_consumption",
        "Global_active_power"
    ]
]


# -----------------------------
# 8. Create processed directory
# -----------------------------
os.makedirs("data/processed", exist_ok=True)


# -----------------------------
# 9. Save processed dataset
# -----------------------------
output_file = "data/processed/energy_processed.csv"

final_df.to_csv(output_file, index=False)

print("Processed dataset saved to:", output_file)
print("Final shape:", final_df.shape)

print("\nFirst 5 rows:")
print(final_df.head())