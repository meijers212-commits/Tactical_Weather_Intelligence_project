from fastapi import FastAPI
from app.py import router
app = FastAPI()

app.include_router(router)



if __name__=="main":
    import uvicorn
    uvicorn.run("main:app", port=5000, host="localhost", reload=True)






    



