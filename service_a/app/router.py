from fastapi import APIRouter
from modols import GetWeatherData
import requests
from dotenv import load_dotenv
import os 

load_dotenv()

host = os.getenv("SERVIS_B_HOST")
port = os.getenv("SERVIS_B_PORT")


router = APIRouter()

@router.post("/ingest")
def post(location: str):
    data = GetWeatherData.ingest_weather_for_location(location)
    url = f"https://{host}/{port}"

    x = requests.post(url, json = data)