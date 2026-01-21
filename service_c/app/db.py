from datetime import datetime
from mysql.connector.connection import MySQLConnectionAbstract
import mysql.connector
from dotenv import load_dotenv
import os


load_dotenv()

db_user = os.getenv("DB_USER")
db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")
db_password = os.getenv("DB_PASSWORD")

# password=db_password

class Dbinstractot:

    @staticmethod
    def get_connection():
        try:
            connection = mysql.connector.connect(
                host=db_host, user=db_user, password=db_password, database=db_name
            )
            return connection

        except Exception as e:
            raise Exception(e)

    @staticmethod
    def creat_table(connection: MySQLConnectionAbstract):
        try:
            # שימוש ב-with מבטיח שהסמן (cursor) ייסגר אוטומטית בסיום
            with connection.cursor() as mycursor:
                mycursor.execute(
                    """
                    CREATE TABLE IF NOT EXISTS records_weather (
                        id INT PRIMARY KEY AUTO_INCREMENT,
                        timestamp DATETIME, 
                        location_name VARCHAR(100),
                        country VARCHAR(100), 
                        latitude FLOAT,
                        longitude FLOAT,
                        temperature FLOAT, 
                        wind_speed FLOAT, 
                        humidity INT,
                        temperature_category VARCHAR(100), 
                        wind_category VARCHAR(100)
                    )
                    """
                )
        except Exception as e:
            raise Exception(f"message:cant create db or db alredy exsisted, Error:{e}")
        
    @staticmethod
    def insert_to_db(data):
        conn = None
        try:
            conn = Dbinstractot.get_connection()
            cursor = conn.cursor(dictionary=True)
            query = """INSERT INTO records_weather(timestamp, location_name, country,
                    latitude, longitude, temperature, wind_speed,
                    humidity, temperature_category, wind_category)
                    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

            for record in data:
                ts_value = record["timestamp"]
                if isinstance(ts_value, str):
                    record["timestamp"] = datetime.fromisoformat(ts_value.replace('Z', ''))

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
                        record["wind_status"],
                    ),
                )
            
            conn.commit()  
            cursor.close()

        except Exception as e:
            if conn:
                conn.rollback() 
            raise Exception(f"message : cant insert data to db successfully, Error:{e}")
        finally:
            if conn:
                conn.close()


