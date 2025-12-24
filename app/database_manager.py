
def mysqlcommand():
    global mydb

    mycursor = mydb.cursor()
    mycursor.execute("DESCRIBE subways")

    for x in mycursor:
        print(x)

def update_screen():
    print("Updating")

def inserting(bmi, diabetes, hypertension, heart_disease,asthma, daily_steps, sleep_hours, stress_level, doctor_visits_per_year, hospital_admissions, medication_count, insurance_coverage_pct, previous_year_cost):
    global mydb
    mycursor = mydb.cursor()

    mycursor.execute("INSERT INTO medical_cost_data (bmi, diabetes, hypertension, heart_disease, asthma, daily_steps, sleep_hours, stress_level, doctor_visits_per_year, hospital_admissions, medication_count, insurance_coverage_pct, previous_year_cost)")
    mydb.commit()

def editing(bmi, diabetes, hypertension, heart_disease,asthma, daily_steps, sleep_hours, stress_level, doctor_visits_per_year, hospital_admissions, medication_count, insurance_coverage_pct, previous_year_cost):
    global mydb
    mycursor = mydb.cursor()

    sql = "UPDATE medical_cost_data SET bmi = %s, diabetes = %s, hypertension = %s, heart_disease = %s, asthma = %s, daily_steps = %s, sleep_hours = %s, stress_level = %s, doctor_visits_per_year = %s, hospital_admissions = %s, medication_count = %s, insurance_coverage_pct = %s, previous_year_cost = %s WHERE id = %i"
    val = bmi, diabetes, hypertension, heart_disease,asthma, daily_steps, sleep_hours, stress_level, doctor_visits_per_year, hospital_admissions, medication_count, insurance_coverage_pct, previous_year_cost

    mycursor.execute(sql, val)
    mydb.commit()

def delete(id):
    global mydb
    mycursor = mydb.cursor()

    mycursor.execute("DELETE FROM medical_cost_data WHERE id = %s", id)

def max_id():
    global mydb
    mycursor = mydb.cursor()

    mycursor.execute("SELECT MAX(id) FROM medical_cost_data")
    return mycursor.fetchone()

def left1():
    id -= 1
    if id < 0:
        id += 1
    update_screen()
def left2():
    id -= 2
    if id < 0:
        id += 2
    update_screen()
def left3():
    id -= 3
    if id < 0:
        id += 3
    update_screen()
def leftEnd():
    id = 0
    update_screen()

def right1():
    id += 1
    if id > max_id():
        id -= 1
    update_screen()
def right2():
    id += 2
    if id > max_id():
        id -= 2
    update_screen()
def right3():
    id += 3
    if id > max_id():
        id -= 3
    update_screen()
def rightEnd():
    id = max_id()
    update_screen()