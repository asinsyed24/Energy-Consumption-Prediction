import pandas as pd
from evidently import Report
from evidently.presets import DataDriftPreset


# --------------------------------
# 1. Load processed energy data
# --------------------------------
data_path = "data/processed/energy_processed.csv"

df = pd.read_csv(data_path)

print("Dataset shape:", df.shape)


# --------------------------------
# 2. Create reference and current data
# --------------------------------
split_index = int(len(df) * 0.8)

reference_data = df.iloc[:split_index].copy()
current_data = df.iloc[split_index:].copy()

print("Reference data:", reference_data.shape)
print("Current data:", current_data.shape)


# --------------------------------
# 3. Select features for monitoring
# --------------------------------
features = [
    "hour",
    "day",
    "month",
    "day_of_week",
    "is_weekend",
    "previous_consumption",
    "Global_active_power"
]

reference_data = reference_data[features]
current_data = current_data[features]


# --------------------------------
# 4. Create Evidently report
# --------------------------------
report = Report(
    metrics=[
        DataDriftPreset()
    ]
)


# --------------------------------
# 5. Run report
# --------------------------------
result = report.run(
    reference_data=reference_data,
    current_data=current_data
)


# --------------------------------
# 6. Save report
# --------------------------------
result.save_html(
    "data_drift_report.html"
)

print("\nData drift report generated successfully!")
print("Saved to: data_drift_report.html")