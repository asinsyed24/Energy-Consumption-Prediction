import pandas as pd
import joblib
import os
import mlflow
import mlflow.sklearn

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# --------------------------------
# 1. Load processed dataset
# --------------------------------
data_path = "data/processed/energy_processed.csv"

df = pd.read_csv(data_path)

print("Dataset shape:", df.shape)


# --------------------------------
# 2. Define features and target
# --------------------------------
features = [
    "hour",
    "day",
    "month",
    "day_of_week",
    "is_weekend",
    "previous_consumption"
]

target = "Global_active_power"

X = df[features]
y = df[target]


# --------------------------------
# 3. Train-test split
# --------------------------------
split_index = int(len(df) * 0.8)

X_train = X.iloc[:split_index]
X_test = X.iloc[split_index:]

y_train = y.iloc[:split_index]
y_test = y.iloc[split_index:]

print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))


# --------------------------------
# 4. MLflow setup
# --------------------------------
mlflow.set_experiment("Energy_Consumption_Prediction")


# --------------------------------
# 5. Start MLflow run
# --------------------------------
with mlflow.start_run():

    # Model parameters
    n_estimators = 100
    max_depth = 15
    random_state = 42

    # Log parameters
    mlflow.log_param("model", "RandomForestRegressor")
    mlflow.log_param("n_estimators", n_estimators)
    mlflow.log_param("max_depth", max_depth)
    mlflow.log_param("random_state", random_state)

    # --------------------------------
    # 6. Create model
    # --------------------------------
    model = RandomForestRegressor(
        n_estimators=n_estimators,
        max_depth=max_depth,
        random_state=random_state,
        n_jobs=-1
    )

    # --------------------------------
    # 7. Train
    # --------------------------------
    print("\nTraining Random Forest model...")

    model.fit(X_train, y_train)

    print("Training completed.")

    # --------------------------------
    # 8. Predictions
    # --------------------------------
    y_pred = model.predict(X_test)

    # --------------------------------
    # 9. Evaluation
    # --------------------------------
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = mse ** 0.5
    r2 = r2_score(y_test, y_pred)

    print("\nModel Performance")
    print("-------------------------")
    print("MAE :", mae)
    print("RMSE:", rmse)
    print("R2  :", r2)

    # --------------------------------
    # 10. Log metrics to MLflow
    # --------------------------------
    mlflow.log_metric("MAE", mae)
    mlflow.log_metric("RMSE", rmse)
    mlflow.log_metric("R2", r2)

    # --------------------------------
    # 11. Save model
    # --------------------------------
    os.makedirs("models", exist_ok=True)

    model_path = "models/energy_model.pkl"

    joblib.dump(model, model_path)

    print("\nModel saved to:", model_path)

    # --------------------------------
    # 12. Log model to MLflow
    # --------------------------------
    mlflow.sklearn.log_model(
        model,
        name="energy_model"
    )

    print("Model logged to MLflow.")