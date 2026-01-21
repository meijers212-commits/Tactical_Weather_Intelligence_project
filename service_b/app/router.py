from fastapi import APIRouter , Body
from dotenv import load_dotenv
import os
from pydantic import BaseModel 
from modols import CleanData

class Records(BaseModel):
    data: list[dict]

load_dotenv()

host = os.getenv("SERVIS_C_HOST")
port = os.getenv("SERVIS_C_PORT")

router = APIRouter()

@router.post("/clean")
def post(records: Records ):
    # data = CleanData.complited_task(records.data)
    # url = f"https://{host}:{port}"
    # x = requests.post(url, json = data)
    print(records.data)
    return {"hi":"hi from server b"}