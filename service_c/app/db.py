from mysql.connector.connection import MySQLConnectionAbstract
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

db_user = os.getenv("DB_USER")
db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")

class Dbinstractot:

    @staticmethod
    def get_connection():
        connection = mysql.connector.connect(
        host=db_host,
        user=db_user,
        database=db_name)
        return connection
    

    @staticmethod
    def creat_table(connection:MySQLConnectionAbstract):
        mycursor = connection.cursor()
        mycursor.execute("""
        CREATE TABLE IF NOT EXIST records_weather (
                        id INT PRIMARY KEY AUTO_INCREMENT,
                        timestamp DATETIME, 
                        location_name VARCHAR(100),
                        country VARCHAR(100), 
                        latitude FLOAT,
                        longitude FLOAT,
                        temperature FLOAT, 
                        wind_speed FLOAT, 
                        humidity INT ,
                        temperature_category VARCHAR(100), 
                        wind_category VARCHAR(100))""")
        
    @staticmethod
    def insert_to_db(data):
        pass
        

   






