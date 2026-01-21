from fastapi import APIRouter
from pydantic import BaseModel 



class Records(BaseModel):
    data: list[dict]





router = APIRouter()

@router.post("/records")
def post(records: Records):
    data1 = records.data
    print(data1[0]["timestamp"])
    return {"hi":"hi from server c"}