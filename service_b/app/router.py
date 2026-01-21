from fastapi import APIRouter , Body
from dotenv import load_dotenv
import os
from pydantic import BaseModel 
from modols import CleanData
import requests

class Records(BaseModel):
    data: list[dict]

load_dotenv()

host = os.getenv("SERVIS_C_HOST")
port = os.getenv("SERVIS_C_PORT")

router = APIRouter()

@router.post("/clean")
def post(records: Records ):
    data = CleanData.complited_task(records.data)
    url = f"http://{host}:{port}/records"
    x = requests.post(url, json = data)
    return x.json()