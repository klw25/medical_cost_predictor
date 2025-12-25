from sql_connect import connect_db, disconnect_db, initialize_id
from model_manager import *

mm = ModelManager()

class DatabaseManager:
    '''def __init__(self):
        self.mydb = connect_db()
        self.mycursor = None
        self.current_id = initialize_id()'''

    def open(self):
        self.mydb = connect_db()
        self.mycursor = None
        self.current_id = initialize_id()
    
    def clear(self,bmiEntry, diabetesEntry, hypertensionEntry, heartDiseaseEntry, asthmaEntry, dailyStepsEntry, sleepHoursEntry, stressLevelsEntry, annualDoctorVisitsEntry, hospitalAdmissionsEntry, medicationCountEntry, insuranceCoverageEntry, previousYearCostEntry, predictedAnnualMedicalCostEntry):
        bmiEntry.delete(0, 'end')
        diabetesEntry.delete(0, 'end')
        hypertensionEntry.delete(0, 'end')
        heartDiseaseEntry.delete(0, 'end')
        asthmaEntry.delete(0, 'end')
        dailyStepsEntry.delete(0, 'end')
        sleepHoursEntry.delete(0, 'end')
        stressLevelsEntry.delete(0, 'end')
        annualDoctorVisitsEntry.delete(0, 'end')
        hospitalAdmissionsEntry.delete(0, 'end')
        medicationCountEntry.delete(0, 'end')
        insuranceCoverageEntry.delete(0, 'end')
        previousYearCostEntry.delete(0, 'end')
        predictedAnnualMedicalCostEntry.delete(0, 'end')

    def mysqlcommand(self):
        mycursor = self.mydb.cursor()
        mycursor.execute("DESCRIBE medical_cost_data")

        for x in mycursor:
            print(x)
        
        mycursor.fetchall()
        mycursor.close()

    def yes_or_no_output(self, number):
        if number == 0:
            return 'No'
        elif number == 1:
            return 'Yes'
    def yes_or_no_input(self, entry):
        if entry == 'No':
            return 0
        elif entry == 'Yes':
            return 1

    def update_screen(self,bmiEntry, diabetesEntry, hypertensionEntry, heartDiseaseEntry, asthmaEntry, dailyStepsEntry, sleepHoursEntry, stressLevelsEntry, annualDoctorVisitsEntry, hospitalAdmissionsEntry, medicationCountEntry, insuranceCoverageEntry, previousYearCostEntry, predictedAnnualMedicalCostEntry):
        
        mycursor = self.mydb.cursor()
        print(f"Current ID: {self.current_id}")
        mycursor.execute("SELECT * FROM medical_cost_data WHERE id = %s", (self.current_id,))
        self.clear(bmiEntry, diabetesEntry, hypertensionEntry, heartDiseaseEntry, asthmaEntry, dailyStepsEntry, sleepHoursEntry, stressLevelsEntry, annualDoctorVisitsEntry, hospitalAdmissionsEntry, medicationCountEntry, insuranceCoverageEntry, previousYearCostEntry, predictedAnnualMedicalCostEntry)
        data = mycursor.fetchone()
        bmiEntry.insert(0, data[1])
        diabetesEntry.insert(0, self.yes_or_no_output(data[2]))
        hypertensionEntry.insert(0, self.yes_or_no_output(data[3]))
        heartDiseaseEntry.insert(0, self.yes_or_no_output(data[4]))
        asthmaEntry.insert(0, self.yes_or_no_output(data[5]))
        dailyStepsEntry.insert(0, data[6])
        sleepHoursEntry.insert(0, data[7])
        stressLevelsEntry.insert(0, data[8])
        annualDoctorVisitsEntry.insert(0, data[9])
        hospitalAdmissionsEntry.insert(0, data[10])
        medicationCountEntry.insert(0, data[11])
        insuranceCoverageEntry.insert(0, data[12])
        previousYearCostEntry.insert(0, data[13])
        predictedAnnualMedicalCostEntry(0, data[14])

        mycursor.fetchall()
        mycursor.close()
        

    def inserting(self,bmi, diabetes, hypertension, heart_disease,asthma, daily_steps, sleep_hours, stress_level, doctor_visits_per_year, hospital_admissions, medication_count, insurance_coverage_pct, previous_year_cost):
        mycursor = self.mydb.cursor()

        mycursor.execute("INSERT INTO medical_cost_data (bmi, diabetes, hypertension, heart_disease, asthma, daily_steps, sleep_hours, stress_level, doctor_visits_per_year, hospital_admissions, medication_count, insurance_coverage_pct, previous_year_cost) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (bmi, self.yes_or_no_input(diabetes), self.yes_or_no_input(hypertension), self.yes_or_no_input(heart_disease), self.yes_or_no_input(asthma), daily_steps, sleep_hours, stress_level, doctor_visits_per_year, hospital_admissions, medication_count, insurance_coverage_pct, previous_year_cost))
        self.mydb.commit()

        mycursor.fetchall()
        mycursor.close()

    def editing(self,bmi, diabetes, hypertension, heart_disease,asthma, daily_steps, sleep_hours, stress_level, doctor_visits_per_year, hospital_admissions, medication_count, insurance_coverage_pct, previous_year_cost):
        mycursor = self.mydb.cursor()

        sql = "UPDATE medical_cost_data SET bmi = %s, diabetes = %s, hypertension = %s, heart_disease = %s, asthma = %s, daily_steps = %s, sleep_hours = %s, stress_level = %s, doctor_visits_per_year = %s, hospital_admissions = %s, medication_count = %s, insurance_coverage_pct = %s, previous_year_cost = %s WHERE id = %s"
        val = (bmi, self.yes_or_no_input(diabetes), self.yes_or_no_input(hypertension), self.yes_or_no_input(heart_disease), self.yes_or_no_input(asthma), daily_steps, sleep_hours, stress_level, doctor_visits_per_year, hospital_admissions, medication_count, insurance_coverage_pct, previous_year_cost, self.current_id)

        mycursor.execute(sql, val)
        self.mydb.commit()

        mycursor.fetchall()
        mycursor.close()

    def delete(self):
        mycursor = self.mydb.cursor()

        val = (self.current_id,)
        mycursor.execute("DELETE FROM medical_cost_data WHERE id = %s", val)
        mycursor.execute("UPDATE medical_cost_data SET id = id - 1 WHERE id > %s", val)
        mycursor.execute(f"ALTER TABLE medical_cost_data AUTO_INCREMENT = {self.max_id() + 1}")

        mycursor.fetchall()
        mycursor.close()

    def input_prediction(self):
        mycursor = self.mydb.cursor()

        mm.load_model()
        predicted_cost = mm.predict_cost(self, self.current_id)

        mycursor.execute("UPDATE medical_cost_data SET annual_medical_cost = %s WHERE id = %s", (predicted_cost, self.current_id))
        self.mydb.commit()

        mycursor.fetchall()
        mycursor.close()

    def max_id(self):        
        mycursor = self.mydb.cursor()

        mycursor.execute("SELECT MAX(id) FROM medical_cost_data")

        max_id = mycursor.fetchone()

        mycursor.fetchall()
        mycursor.close()
        return max_id[0]

    def left1(self):
        self.current_id -= 1
        if self.current_id < 1:
            self.current_id += 1
    def left2(self):
        self.current_id -= 2
        if self.current_id < 1:
            self.current_id += 2
    def left3(self):
        self.current_id -= 3
        if self.current_id < 1:
            self.current_id += 3
    def leftEnd(self):
        self.current_id = 1

    def right1(self):
        self.current_id += 1
        if self.current_id > self.max_id():
            self.current_id -= 1
    def right2(self):
        self.current_id += 2
        if self.current_id > self.max_id():
            self.current_id -= 2
    def right3(self):
        self.current_id += 3
        if self.current_id > self.max_id():
            self.current_id -= 3
    def rightEnd(self):
        self.current_id = self.max_id()
    def close(self, bmiEntry, diabetesEntry, hypertensionEntry, heartDiseaseEntry, asthmaEntry, dailyStepsEntry, sleepHoursEntry, stressLevelsEntry, annualDoctorVisitsEntry, hospitalAdmissionsEntry, medicationCountEntry, insuranceCoverageEntry, previousYearCostEntry, predictedAnnualMedicalCostEntry):
        if self.mydb:
            disconnect_db(self.mydb)
            self.mydb = None
            self.mycursor = None
            self.clear(bmiEntry, diabetesEntry, hypertensionEntry, heartDiseaseEntry, asthmaEntry, dailyStepsEntry, sleepHoursEntry, stressLevelsEntry, annualDoctorVisitsEntry, hospitalAdmissionsEntry, medicationCountEntry, insuranceCoverageEntry, previousYearCostEntry, predictedAnnualMedicalCostEntry)