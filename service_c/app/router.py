from fastapi import APIRouter
from pydantic import BaseModel 


class Records(BaseModel):
    data: list[dict]

router = APIRouter()

@router.post("/records")
def post(records: Records):
    data1 = records.data
    return {"hi":"hi from server c"}


@router.get("/records")
def get_records_by_time_or_location(time_or_location):
    pass

@router.get("/records/count")
def get_records_number_by_locations():
    pass

@router.get("/records/avg-temperature")
def get_evg_temp_by_locations():
    pass

@router.get("/records/max-wind")
def get_max_wind_spid_by_locations():
    pass

@router.get("/records/extreme")
def get_extreme_locations():
    pass


# ==================================================
# from datetime import datetime

# dt = datetime.fromisoformat(s)


# cursor.execute(
#     "INSERT INTO events (created_at) VALUES (%s)",
#     (dt,)
# )

