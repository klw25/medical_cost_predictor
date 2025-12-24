import mysql.connector

def connect_db():

    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="030579",
    database="medical_data"
    )
    return mydb


def disconnect_db(mydb):
    mydb.close()

def initialize_id():
    current_id = 1
    return current_id