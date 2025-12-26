from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

import pandas as pd
import matplotlib.pyplot as plt

from get_mae import get_mae
from data import load_data

def run_pipeline():

    medical_cost_data = load_data()
    medical_cost_data = pd.get_dummies(medical_cost_data, drop_first=True)

    y = medical_cost_data.annual_medical_cost
    features = ['bmi', 'diabetes', 'hypertension', 'heart_disease','asthma', 'daily_steps', 'sleep_hours', 'stress_level', 'doctor_visits_per_year', 'hospital_admissions', 'medication_count', 'insurance_coverage_pct', 'previous_year_cost']

    X = medical_cost_data[features]

    train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

    #Calculate the best mae
    #__________________________________________________________________________________________
    max_leaf_nodes = [5, 25, 50, 100, 250, 500, 600, 700, 1000, 10000]

    mae = 10000000000000000000000
    ideal = 0
    for max_leaf_nodes in max_leaf_nodes:
        if mae > get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
            mae = get_mae(max_leaf_nodes,train_X, val_X, train_y, val_y)
            ideal = max_leaf_nodes



    #Calculate the mae
    #__________________________________________________________________________________________

    medical_cost_model = DecisionTreeRegressor(max_leaf_nodes=ideal, random_state=1)
    medical_cost_model.fit(X, y)
    val_predictions = medical_cost_model.predict(val_X)
    val_mae = mean_absolute_error(val_predictions, val_y)
    print(f"Validation MAE: {val_mae}")

    #Complete Model
    #____________________________________________________________________________________________
    rf_medical_cost_model = RandomForestRegressor(max_leaf_nodes=ideal, random_state=1)
    rf_medical_cost_model.fit(X, y)
    predictions = rf_medical_cost_model.predict(val_X)

    #Comparison
    #_____________________________________________________________________________________________
    comparison = pd.DataFrame({'Actual': val_y.head().tolist(), 'Predicted': predictions[:5]})
    print("\nFirst 5 Predictions vs Actuals:")
    print(comparison)

    #matplotlib
    #____________________________________________________________________________________________
    plt.figure(figsize=(10, 6))
    plt.scatter(val_y, predictions, alpha=0.5)
    plt.plot([val_y.min(), val_y.max()], [val_y.min(), val_y.max()], 'k--', lw=2)
    plt.xlabel('Actual Medical Cost')
    plt.ylabel('Predicted Medical Cost')
    plt.title('Actual vs. Predicted Medical Costs (Random Forest)')
    plt.show()

    return rf_medical_cost_model