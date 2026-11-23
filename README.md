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

## Azure Cloud Deployment

The Energy Consumption Prediction system is deployed on Microsoft Azure using Azure Container Apps.

### Live Application

- **Streamlit Frontend:** https://energy-streamlit-app.politesky-e2ec2cbb.centralindia.azurecontainerapps.io/
- **FastAPI Backend:** https://energy-api-app.politesky-e2ec2cbb.centralindia.azurecontainerapps.io/
- **API Documentation:** https://energy-api-app.politesky-e2ec2cbb.centralindia.azurecontainerapps.io/docs

### Deployment Architecture

1. The user enters energy consumption details through the Streamlit interface.
2. Streamlit sends the input data to the FastAPI backend.
3. FastAPI loads the trained machine learning model.
4. The model predicts energy consumption.
5. The prediction is displayed on the Streamlit dashboard.

### Azure Services Used

- Azure Container Registry (ACR)
- Azure Container Apps
- Azure Container Apps Environment
- Azure Resource Group

### Docker Containers

- `energy-api`: FastAPI prediction service.
- `energy-streamlit`: Streamlit frontend application.

### Project Features

- Energy consumption prediction
- Interactive Streamlit dashboard
- REST API using FastAPI
- Historical energy consumption visualization
- Model monitoring using Evidently AI
- Experiment tracking using MLflow
- Data versioning using DVC
- CI using GitHub Actions
