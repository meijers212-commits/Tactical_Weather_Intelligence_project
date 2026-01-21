from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.db import Dbinstractot
from app.modols import DataManipulation

class Records(BaseModel):
    data: list[dict]


router = APIRouter()


@router.post("/records")
def post(records: Records):
    try:

        data1 = records.data
        conn = Dbinstractot.get_connection()
        Dbinstractot.creat_table(connection=conn)
        Dbinstractot.insert_to_db(data=data1)
        return {"message": "data inserted succefully"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/records")
def get_records_by_time_or_location(time_or_location):
    try:
        data = DataManipulation.get_by_time_or_location(time_or_location)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/records/count")
def get_records_number_by_locations():
    try:
        data = DataManipulation.records_number_by_location()
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/records/avg-temperature")
def get_evg_temp_by_locations():
    try:
        data = DataManipulation.get_evg_temp_by_erea()
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/records/max-wind")
def get_max_wind_spid_by_locations():
    try:
        data = DataManipulation.get_max_wind_by_location()
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/records/extreme")
def get_extreme_locations():
    try:
        data = DataManipulation.get_extrime_locations()
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
