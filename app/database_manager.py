from sql_connect import connect_db, disconnect_db
id = 0
#CHANGE ALL TO self.

class DatabaseManager:
    def __init__(self):
        self.mydb = connect_db()
        self.mycursor = None

    def mysqlcommand(self):
        mycursor = self.mydb.cursor()
        mycursor.execute("DESCRIBE medical_cost_data")

        for x in mycursor:
            print(x)

    def update_screen(self,bmiEntry, diabetesEntry, hypertensionEntry, heartDiseaseEntry, asthmaEntry, dailyStepsEntry, sleepHoursEntry, stressLevelsEntry, annualDoctorVisitsEntry, hospitalAdmissionsEntry, medicationCountEntry, insuranceCoverageEntry, previousYearCostEntry):
        global id
        
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT * FROM medical_cost_data", id)

        data = mycursor.fetchone()
        bmiEntry.delete(0, 'end')
        bmiEntry.insert(0, data[1])
        diabetesEntry.delete(0, 'end')
        diabetesEntry.insert(0, data[2])
        hypertensionEntry.delete(0, 'end')
        hypertensionEntry.insert(0, data[3])
        heartDiseaseEntry.delete(0, 'end')
        heartDiseaseEntry.insert(0, data[4])
        asthmaEntry.delete(0, 'end')
        asthmaEntry.insert(0, data[5])
        dailyStepsEntry.delete(0, 'end')
        dailyStepsEntry.insert(0, data[6])
        sleepHoursEntry.delete(0, 'end')
        sleepHoursEntry.insert(0, data[7])
        stressLevelsEntry.delete(0, 'end')
        stressLevelsEntry.insert(0, data[8])
        annualDoctorVisitsEntry.delete(0, 'end')
        annualDoctorVisitsEntry.insert(0, data[9])
        hospitalAdmissionsEntry.delete(0, 'end')
        hospitalAdmissionsEntry.insert(0, data[10])
        medicationCountEntry.delete(0, 'end')
        medicationCountEntry.insert(0, data[11])
        insuranceCoverageEntry.delete(0, 'end')
        insuranceCoverageEntry.insert(0, data[12])
        previousYearCostEntry.delete(0, 'end')
        previousYearCostEntry.insert(0, data[13])
        

    def inserting(self,bmi, diabetes, hypertension, heart_disease,asthma, daily_steps, sleep_hours, stress_level, doctor_visits_per_year, hospital_admissions, medication_count, insurance_coverage_pct, previous_year_cost):
        
        global id
        mycursor = self.mydb.cursor()

        mycursor.execute("INSERT INTO medical_cost_data (bmi, diabetes, hypertension, heart_disease, asthma, daily_steps, sleep_hours, stress_level, doctor_visits_per_year, hospital_admissions, medication_count, insurance_coverage_pct, previous_year_cost) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (bmi, diabetes, hypertension, heart_disease, asthma, daily_steps, sleep_hours, stress_level, doctor_visits_per_year, hospital_admissions, medication_count, insurance_coverage_pct, previous_year_cost))
        self.mydb.commit()

    def editing(self,bmi, diabetes, hypertension, heart_disease,asthma, daily_steps, sleep_hours, stress_level, doctor_visits_per_year, hospital_admissions, medication_count, insurance_coverage_pct, previous_year_cost):
        
        global id
        mycursor = self.mydb.cursor()

        sql = "UPDATE medical_cost_data SET bmi = %s, diabetes = %s, hypertension = %s, heart_disease = %s, asthma = %s, daily_steps = %s, sleep_hours = %s, stress_level = %s, doctor_visits_per_year = %s, hospital_admissions = %s, medication_count = %s, insurance_coverage_pct = %s, previous_year_cost = %s WHERE id = %i"
        val = bmi, diabetes, hypertension, heart_disease,asthma, daily_steps, sleep_hours, stress_level, doctor_visits_per_year, hospital_admissions, medication_count, insurance_coverage_pct, previous_year_cost, id

        mycursor.execute(sql, val)
        self.mydb.commit()

    def delete(self):
        
        global id
        mycursor = self.mydb.cursor()

        mycursor.execute("DELETE FROM medical_cost_data WHERE id = %s", id)

    def max_id(self):
        
        mycursor = self.mydb.cursor()

        mycursor.execute("SELECT MAX(id) FROM medical_cost_data")
        return mycursor.fetchone()

    def left1(self):
        global id
        id -= 1
        if id < 0:
            id += 1
    def left2(self):
        global id
        id -= 2
        if id < 0:
            id += 2
    def left3(self):
        global id
        id -= 3
        if id < 0:
            id += 3
    def leftEnd(self):
        global id
        id = 0

    def right1(self):
        global id
        id += 1
        if id > self.max_id():
            id -= 1
    def right2(self):
        global id
        id += 2
        if id > self.max_id():
            id -= 2
    def right3(self):
        global id
        id += 3
        if id > self.max_id():
            id -= 3
    def rightEnd(self):
        global id
        id = self.max_id()
    def close(self):
        if self.mydb:
            disconnect_db()