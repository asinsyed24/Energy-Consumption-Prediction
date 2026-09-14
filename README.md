# Energy Consumption Prediction with MLOps

## 📌 Project Overview

Energy Consumption Prediction is an end-to-end Machine Learning and MLOps project that predicts household energy consumption using historical electricity consumption data.

The project uses a Random Forest Regressor and integrates MLOps tools for data versioning, experiment tracking, monitoring, continuous integration, containerization, and deployment.

---

## 🎯 Objectives

- Predict household energy consumption.
- Version the dataset using DVC.
- Store DVC data remotely using DagsHub.
- Track ML experiments using MLflow.
- Monitor data drift using Evidently AI.
- Build a REST API using FastAPI.
- Create a user interface using Streamlit.
- Containerize the application using Docker.
- Implement CI using GitHub Actions.
- Deploy the application using Render.

---

## 🏗️ MLOps Architecture

```text
                    ┌─────────────────────┐
                    │   Household Energy  │
                    │       Dataset       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │        DVC          │
                    │ Data Versioning     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      DagsHub        │
                    │ Remote Data Storage │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Data Preparation    │
                    │  & Feature Creation │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Random Forest       │
                    │     Regressor       │
                    └──────────┬──────────┘
                               │
                 ┌─────────────┴─────────────┐
                 ▼                           ▼
       ┌─────────────────┐         ┌─────────────────┐
       │     MLflow      │         │    Evidently    │
       │ Experiment      │         │  Data Drift     │
       │ Tracking        │         │   Monitoring    │
       └─────────────────┘         └─────────────────┘
                 │
                 ▼
       ┌─────────────────┐
       │     FastAPI     │
       │   REST API      │
       └────────┬────────┘
                │
                ▼
       ┌─────────────────┐
       │    Streamlit    │
       │   Web Interface │
       └────────┬────────┘
                │
                ▼
       ┌─────────────────┐
       │     Docker      │
       │   Container     │
       └────────┬────────┘
                │
                ▼
       ┌─────────────────┐
       │     Render      │
       │    Deployment   │
       └─────────────────┘

       GitHub Actions → Continuous Integration
