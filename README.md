#  House Price Prediction - End-to-End Data Science Project

##  Problem Statement

The goal of this project is to build a machine learning model that can predict house prices based on various features such as number of bedrooms, bathrooms, square footage, and floors. This helps buyers and sellers estimate property values accurately.

##  Dataset Details

* Dataset: House Sales Prediction Dataset (Kaggle)
* Features include:

  * Bedrooms
  * Bathrooms
  * Square Footage
  * Floors
  * Location attributes
* Target Variable:

  * Price (House Price)

##  Approach

### 1. Data Collection

* Dataset downloaded from Kaggle and loaded into Google Colab

### 2. Data Cleaning

* Removed unnecessary columns (`id`, `date`)
* Handled missing values
* Checked data types

### 3. Exploratory Data Analysis (EDA)

* Correlation heatmap
* Distribution plots
* Identified important features affecting price

### 4. Model Building

* Used Linear Regression model
* Split data into training and testing sets
* Trained model using scikit-learn

### 5. Model Evaluation

* Metrics used:

  * Mean Absolute Error (MAE)
  * R² Score

### 6. Deployment

* Built a Streamlit web app
* User inputs house details
* Model predicts house price instantly

##  Results

* The model successfully predicts house prices based on input features
* Achieved good R² score indicating strong performance
* Deployed using Streamlit for real-time predictions

##  Features

✔ End-to-End Data Science Workflow
✔ Clean and simple UI using Streamlit
✔ Real-time prediction
✔ Beginner-friendly project

##  Author

Mahi Savani
