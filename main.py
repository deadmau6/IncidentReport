from fastapi import FastAPI
from api import incidents

app = FastAPI()

app.include_router(incidents.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}