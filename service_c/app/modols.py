from db import Dbinstractot as db


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
                cursor.execute(query, (time))
                result = cursor.fetchall()
                cursor.close()
                conn.close()
            else:
                location = time_or_location
                query = "SELECT * FROM records_weather WHERE location_name = %s "
                cursor.execute(query, (location))
                result = cursor.fetchall()
                cursor.close()
                conn.close()
            return result
        except Exception as e:
            raise {"message": f"cudent get data by tyme/location, Error{e}"}

    @staticmethod
    def records_number_by_location():
        try:
            conn = db.get_connection()
            cursor = conn.cursor(dictionary=True)
            query = "SELECT location_name, count(*) as record_numbers FROM records_weather GROUPBY location_name"
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            conn.close()
            return result
        except Exception as e:
            raise {"message": f"cudet get records by location, Error: {e}"}

    @staticmethod
    def get_evg_temp_by_erea():
        try:

            conn = db.get_connection()
            cursor = conn.cursor(dictionary=True)
            query = "SELECT location_name, evg(temperature) as avg_temp FROM records_weather GROUPBY location_name"
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            conn.close()
            return result

        except Exception as e:
            raise {"message": f"codent get evg temp by erea, Error:{e}"}


    @staticmethod
    def get_max_wind_by_location():
        try:

            conn = db.get_connection()
            cursor = conn.cursor(dictionary=True)
            query = "SELECT location_name, max(wind_speed) as max_wind FROM records_weather GROUPBY location_name"
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            conn.close()
            return result

        except Exception as e:
            raise {"message": f"codent get max wind by erea, Error:{e}"}
# try:

#         except Exception as e:
#             raise {"message" : f"codent get evg temp by erea, Error:{e}"}
