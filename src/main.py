import os
from fastapi import FastAPI
from src.excel import controller
from mangum import Mangum

app = FastAPI()

handler = None

app.include_router(router=controller.router, prefix='/excel', tags=['excel'])

@app.get("/")
async def root():
    return {"message": "Hello World"}

if os.getenv('ENVIRONMENT_TYPE') == 'SERVERLESS':
   handler = Mangum(app=app, lifespan="off")