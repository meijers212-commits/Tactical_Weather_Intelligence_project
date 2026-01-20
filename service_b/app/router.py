from fastapi import APIRouter
from modols import GetWeatherData
import requests
from dotenv import load_dotenv
import os 
from modols import CleanData

load_dotenv()

host = os.getenv("SERVIS_C_HOST")
port = os.getenv("SERVIS_c_PORT")
print(host,port)

router = APIRouter()

@router.post("/clean")
def post(clean):
    data = CleanData.complited_task(clean)
    url = f"https://{host}/{port}"
    x = requests.post(url, json = data)