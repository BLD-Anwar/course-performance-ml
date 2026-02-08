# Course Performance Monitoring and Pass/Fail Prediction System

This project predicts whether a student will pass or fail a course using machine learning.

## Folder Structure

DATA/ - Scripts to generate and store data  
MODELS/ - Model training and prediction scripts  
APP/ - Dashboard application  
UTILS/ - Helper functions 



Course Performance Monitoring and Pass or Fail Prediction System


Project Overview

This project builds a machine learning system to monitor student course performance and predict whether a student is likely to pass or fail. The system uses synthetic academic data stored in a SQL database, trains a classification model, and provides a dashboard for analysis and predictions.


Problem Statement

In universities, students who are academically at risk are often identified too late. This project aims to predict student performance early using data such as attendance, assignment scores, quiz results, and midterm marks. Early predictions can help faculty take timely academic interventions.

Solution Approach

The system simulates a university academic environment using synthetic data. The data is stored in a structured SQL database and used to train a machine learning model. A dashboard is developed to visualize performance trends and allow predictions for new student inputs. The model can be retrained as new data becomes available.


Tech Stack

Python

SQLite (SQL database)

Pandas, NumPy

Scikit-learn

Streamlit (Dashboard)

Matplotlib

Git & GitHub (Version Control)



How to Run the Project
1. Install dependencies
pip install pandas scikit-learn streamlit matplotlib joblib

2. Generate Data
python data/generate_data.py


This creates the SQL database and inserts synthetic student records.

3. Train the Model
python models/train_model.py


This trains the model and saves it in the models folder.

4. Run the Dashboard
streamlit run app/app.py


The dashboard will open in your browser showing data analysis and prediction features.

Model Lifecycle

As new academic data becomes available, the model can be retrained using updated records from the database. Future versions of the system will automate retraining and maintain model version history.

Notes

The dataset is synthetically generated because real student data is private and not accessible.

This project focuses on building a complete machine learning deployment pipeline rather than only improving model accuracy.