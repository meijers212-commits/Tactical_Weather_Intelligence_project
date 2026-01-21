from fastapi import APIRouter
from app.modols import GetWeatherData
import requests
from dotenv import load_dotenv
import os
from pydantic import BaseModel

class Records(BaseModel):
    data: list[dict]

load_dotenv()

host = os.getenv("SERVIS_B_HOST")
port = os.getenv("SERVIS_B_PORT")


router = APIRouter()


@router.post("/ingest")
def post(location: str):
    data = Records(data=GetWeatherData.ingest_weather_for_location(location))
    url = f"http://{host}:{port}/clean"
    x = requests.post(url, json=data.model_dump(mode='json'))
    return x.json()
