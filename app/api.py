from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd


# --------------------------------
# 1. Create FastAPI application
# --------------------------------
app = FastAPI(
    title="Energy Consumption Prediction API",
    description="API for predicting household energy consumption",
    version="1.0"
)


# --------------------------------
# 2. Load trained model
# --------------------------------
model = joblib.load("models/energy_model.pkl")


# --------------------------------
# 3. Define input data
# --------------------------------
class EnergyInput(BaseModel):

    hour: int
    day: int
    month: int
    day_of_week: int
    is_weekend: int
    previous_consumption: float


# --------------------------------
# 4. Home endpoint
# --------------------------------
@app.get("/")
def home():
    return {
        "message": "Energy Consumption Prediction API is running"
    }


# --------------------------------
# 5. Prediction endpoint
# --------------------------------
@app.post("/predict")
def predict(data: EnergyInput):

    input_data = pd.DataFrame(
        [[
            data.hour,
            data.day,
            data.month,
            data.day_of_week,
            data.is_weekend,
            data.previous_consumption
        ]],
        columns=[
            "hour",
            "day",
            "month",
            "day_of_week",
            "is_weekend",
            "previous_consumption"
        ]
    )

    prediction = model.predict(input_data)

    return {
        "predicted_energy_consumption": round(
            float(prediction[0]), 3
        )
    }