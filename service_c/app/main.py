from fastapi import FastAPI
from router import router

app = FastAPI()

app.include_router(router)



if __name__=="__main__":
    import uvicorn
    uvicorn.run("main:app", port=8081, host="localhost", reload=True)



# ==================================================
# from datetime import datetime

# dt = datetime.fromisoformat(s)


# cursor.execute(
#     "INSERT INTO events (created_at) VALUES (%s)",
#     (dt,)
# )



    



