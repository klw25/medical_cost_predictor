import mysql.connector

def connect_db():
    global mydb

    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="030579",
    database="medical_data"
    )

def disconnect_db():
    global mydb
    
    mydb.close()