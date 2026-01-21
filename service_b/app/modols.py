import pandas as pd
from pydantic import BaseModel 

class Records(BaseModel):
    data: list[dict]
    
class CleanData():

    @staticmethod
    def convert_to_df(data):
        df = pd.DataFrame(data=data)
        return df

    @staticmethod
    def Add_important_columns(df):
        df["temperature_category"] = pd.cut(df["temperature"],[0,18,25,float("inf")],labels=["cold", "moderate", "hot"],include_lowest=True)
        df["wind_status"] = pd.cut(df["wind_speed"],[0,10,float("inf")],labels=["calm", "windy"],include_lowest=True)
        return df
    
    @staticmethod
    def convert_df_to_json(df):
        # convert df to Records list[dict]!!
        data = Records(data=df)
        return data.model_dump(mode="json")

    @staticmethod
    def complited_task(data):
        df = CleanData.convert_to_df(data)
        df1 = CleanData.Add_important_columns(df)
        json_data = CleanData.convert_df_to_json(df1)
        return json_data