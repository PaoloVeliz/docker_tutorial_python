import os
from dotenv import load_dotenv
import mysql.connector

class Tables:
    def fetch_all_data_from_table_1():
        result = ""
        mydb = mysql.connector.connect(
            host=os.getenv('DATABASE_URL'),
            port=os.getenv('DATABASE_PORT'),
            user=os.getenv('DATABASE_USER'),
            password=os.getenv('DATABASE_PASSWORD'),
            database=os.getenv('DATABASE_NAME')
        )

        mycursor = mydb.cursor()

        mycursor.execute("SELECT * FROM heats")

        myresult = mycursor.fetchall() 

        return myresult


    def fetch_all_data_from_table_2():
        result = ""
        mydb = mysql.connector.connect(
            host=os.getenv('DATABASE_URL'),
            port=os.getenv('DATABASE_PORT'),
            user=os.getenv('DATABASE_USER'),
            password=os.getenv('DATABASE_PASSWORD'),
            database=os.getenv('DATABASE_NAME')
        )

        mycursor = mydb.cursor()

        mycursor.execute("SELECT * FROM tbl_DatosDengue")

        myresult = mycursor.fetchall() 

        return myresult