from db import Dbinstractot as db

class DataManipulation:


    @staticmethod
    def get_by_time_or_location(time_or_location):
        conn = db.get_connection()
        cursor = conn.cursor(dictionary=True)
        if "." in time_or_location or "/" in time_or_location or "-" in time_or_location or "," in time_or_location:
            time = time_or_location
            query = "SELECT * FROM records_weather WHERE timestamp = %s"
            result = cursor.execute(query,(time))
        else:
            location = time_or_location
            query = "SELECT * FROM records_weather WHERE location_name = %s "
            result = cursor.execute(query,(location))
            cursor.close()
            conn.close()
        return result



    @staticmethod
    def records_number_by_location(location):
        conn = db.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = f"SELECT location_name, count(*) as record_numbers FROM records_weather GROUPBY location_name"
        result = cursor.execute(query)
        cursor.close()
        conn.close()
        return result