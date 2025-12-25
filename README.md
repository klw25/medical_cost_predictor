# Medical Cost Predictor
Created by Kenneth Withers - klw25@fsu.edu  

A Python-based desktop application that manages patient health records and uses Machine Learning to predict future medical expenses.

## Overview
This application provides a user-friendly interface for medical professionals or administrators to input patient data (such as BMI, age, smoking status, etc.). It utilizes a **Random Forest** machine learning model, created by myself using existing data from kaggle, to estimate the annual medical cost for each patient based on their health metrics.

The app is connected to a **MySQL database** to persist patient records, allowing for full CRUD (Create, Read, Update, Delete) functionality.
<img width="1319" height="1003" alt="image" src="https://github.com/user-attachments/assets/5278848e-584e-419a-82c5-4fc5148cf1e3" />

## Features
* **Patient Management:** Add, view, update, and delete patient records.
* **AI Cost Prediction:** instantly predict annual medical costs using a pre-trained ML model.
* **Database Integration:** Securely stores all data in a local MySQL database.
* **Search & Navigation:** Easily search for patients by ID or navigate through records one by one.
* **Interactive Dashboard:** Visual interface built with Tkinter.

## Tech Stack
* **Language:** Python 3.12+
* **GUI:** Tkinter
* **Database:** MySQL
* **Machine Learning:** Scikit-Learn, Pandas, NumPy
* **Model Storage:** Joblib

## Installation & Setup

### 1. Prerequisites
Ensure you have the following installed:
* Python 3.x
* MySQL Server (and MySQL Workbench recommended)
* Git

### 2. Clone the Repository
```bash
git clone [https://github.com/yourusername/MedicalCostPrediction.git](https://github.com/yourusername/MedicalCostPrediction.git)
cd MedicalCostPrediction
