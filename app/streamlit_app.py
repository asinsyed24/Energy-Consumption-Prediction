import streamlit as st
import requests
import pandas as pd


# --------------------------------
# Page configuration
# --------------------------------
st.set_page_config(
    page_title="Energy Consumption Predictor",
    page_icon="⚡",
    layout="centered"
)


# --------------------------------
# Title
# --------------------------------
st.title("⚡ Energy Consumption Predictor")

st.write(
    "Enter the household energy information "
    "to predict electricity consumption."
)


# --------------------------------
# Input fields
# --------------------------------
hour = st.number_input(
    "Hour",
    min_value=0,
    max_value=23,
    value=18
)

day = st.number_input(
    "Day",
    min_value=1,
    max_value=31,
    value=16
)

month = st.number_input(
    "Month",
    min_value=1,
    max_value=12,
    value=12
)

day_of_week = st.number_input(
    "Day of Week",
    min_value=0,
    max_value=6,
    value=5
)

is_weekend = st.selectbox(
    "Is it a weekend?",
    options=[0, 1],
    format_func=lambda x: "Yes" if x == 1 else "No"
)

previous_consumption = st.number_input(
    "Previous Hour Consumption (kW)",
    min_value=0.0,
    value=4.2,
    step=0.1
)


# --------------------------------
# Prediction button
# --------------------------------
if st.button("🔮 Predict Energy Consumption"):

    data = {
        "hour": int(hour),
        "day": int(day),
        "month": int(month),
        "day_of_week": int(day_of_week),
        "is_weekend": int(is_weekend),
        "previous_consumption": float(previous_consumption)
    }



    try:

        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=data
        )

        if response.status_code == 200:

            result = response.json()

            prediction = result[
                "predicted_energy_consumption"
            ]

            st.success("Prediction successful!")

            st.metric(
                "Predicted Energy Consumption",
                f"{prediction} kW"
            )

        else:

            st.error(
                f"API Error: {response.status_code}"
            )

    except requests.exceptions.ConnectionError:

        st.error(
            "Could not connect to FastAPI. "
            "Make sure the FastAPI server is running."
        )

# --------------------------------
# Historical Energy Consumption
# --------------------------------

st.subheader("📈 Historical Energy Consumption")

try:

    df = pd.read_csv(
        "data/processed/energy_processed.csv"
    )

    # Display only the most recent 100 hours
    chart_data = df.tail(100).copy()

    st.line_chart(
        chart_data["Global_active_power"]
    )

    st.write(
        "Showing the latest 100 hourly energy consumption records."
    )

except FileNotFoundError:

    st.error(
        "Processed energy dataset not found."
    )