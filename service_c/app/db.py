from datetime import datetime
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
        try:
            connection = mysql.connector.connect(
                host=db_host, user=db_user, database=db_name
            )
            return connection

        except Exception as e:
            raise e

    @staticmethod
    def creat_table(connection: MySQLConnectionAbstract):
        try:
            mycursor = connection.cursor()
            mycursor.execute(
                """
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
                            wind_category VARCHAR(100))"""
            )

        except Exception as e:
            raise {"message": f"cant create db or db alredy exsisted, Error{e}"}

    @staticmethod
    def insert_to_db(data):
        try:
            conn = Dbinstractot.get_connection()
            cursor = conn.cursor(dictionary=True)
            query = """INSERT INTO records_weather(timestamp ,location_name, country,
            latitude, longitude, temperature, wind_speed,
            humidity, temperature_category, wind_category)
            VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

            for record in data:
                record["timestamp"] = datetime.strptime(
                    record["timestamp"], "%Y-%m-%d %H:%M:%S"
                )
                cursor.execute(
                    query,
                    (
                        record["timestamp"],
                        record["location_name"],
                        record["country"],
                        record["latitude"],
                        record["longitude"],
                        record["temperature"],
                        record["wind_speed"],
                        record["humidity"],
                        record["temperature_category"],
                        record["wind_category"],
                    ),
                )

            cursor.close()
            conn.close()

        except Exception as e:
            raise {"message": f"cant enset data to db sexsesfuly, Error:{e}"}
