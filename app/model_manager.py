import joblib
import numpy as np
import os

class ModelManager:
    def load_model(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        model_path = os.path.join(current_dir, 'medical_model.pkl')
        self.model = joblib.load(model_path)

    def predict_cost(self, database_manager, current_id):
        cursor = database_manager.mydb.cursor()
        sql = "SELECT * FROM medical_cost_data WHERE id = %s"
        cursor.execute(sql, (current_id,))
        data = cursor.fetchone()
        cursor.close()

        bmi = float(data[1])
        diabetes_raw = data[2]
        hypertension_raw = data[4]
        heart_disease_raw = data[5]
        asthma_raw = data[6]
        daily_steps = data[7]
        sleep_hours = data[8]
        stress_level = data[9]
        doctor_visits_per_year = data[10]
        hospital_admissions = data[11]
        medication_count = data[12]
        insurance_coverage_pct = data[13]
        previous_year_cost = data[14]

        diabetes = 1 if diabetes_raw == "Yes" else 0
        hypertension = 1 if hypertension_raw == "Yes" else 0
        heart_disease = 1 if heart_disease_raw == "Yes" else 0
        asthma = 1 if asthma_raw == "Yes" else 0

        features = np.array([[bmi, diabetes, hypertension, heart_disease, asthma, daily_steps, sleep_hours, stress_level, doctor_visits_per_year, hospital_admissions, medication_count, insurance_coverage_pct, previous_year_cost]])
        prediction = self.model.predict(features)
        predicted_cost = round(prediction[0], 2)

        return predicted_cost