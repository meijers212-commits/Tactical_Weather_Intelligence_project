from app.db import Dbinstractot as db


class DataManipulation:

    @staticmethod
    def get_by_time_or_location(time_or_location):
        try:
            conn = db.get_connection()
            cursor = conn.cursor(dictionary=True)
            if (
                "." in time_or_location
                or "/" in time_or_location
                or "-" in time_or_location
                or "," in time_or_location
            ):
                time = time_or_location
                query = "SELECT * FROM records_weather WHERE timestamp = %s"
                cursor.execute(query, (time,))
                result = cursor.fetchall()
                cursor.close()
                conn.close()
            else:
                location = time_or_location
                query = "SELECT * FROM records_weather WHERE location_name = %s "
                cursor.execute(query, (location,))
                result = cursor.fetchall()
                cursor.close()
                conn.close()
            return result
        except Exception as e:
            raise Exception(f"message : cudent get data by tyme/location, Error{e}")

    @staticmethod
    def records_number_by_location():
        try:
            conn = db.get_connection()
            cursor = conn.cursor(dictionary=True)
            query = """SELECT location_name, COUNT(*) AS record_numbers 
                    FROM records_weather 
                    GROUP BY location_name;"""
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            conn.close()
            return result
        except Exception as e:
            raise Exception(f"message : cudet get records by location, Error: {e}")

    @staticmethod
    def get_evg_temp_by_erea():
        try:

            conn = db.get_connection()
            cursor = conn.cursor(dictionary=True)
            query = """SELECT location_name, AVG(temperature) AS avg_temp 
                    FROM records_weather 
                    GROUP BY location_name;"""
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            conn.close()
            return result

        except Exception as e:
            raise Exception(f"message : codent get evg temp by erea, Error:{e}")

    @staticmethod
    def get_max_wind_by_location():
        conn = None
        try:
            conn = db.get_connection()
            cursor = conn.cursor(dictionary=True)

            query = """
                SELECT location_name, MAX(wind_speed) AS max_wind 
                FROM records_weather 
                GROUP BY location_name
            """

            cursor.execute(query)
            result = cursor.fetchall()

            cursor.close()
            return result

        except Exception as e:
            raise Exception(f"message: couldn't get max wind by area, Error: {e}")

        finally:
            if conn and conn.is_connected():
                conn.close()

    @staticmethod
    def get_extrime_locations():
        try:

            conn = db.get_connection()
            cursor = conn.cursor(dictionary=True)
            query = """SELECT location_name FROM records_weather
                    WHERE (temperature_category = 'hot' AND wind_status = 'calm')
                    OR (temperature_category = 'cold' AND wind_status = 'windy')"""
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            conn.close()
            return result

        except Exception as e:
            raise Exception(f"message: codent get extreme locations, Error:{e}")
