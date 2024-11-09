from fastapi import FastAPI
from src.excel import controller

app = FastAPI()

app.include_router(router=controller.router, prefix='/excel', tags=['excel'])

@app.get("/")
async def root():
    return {"message": "Hello World"}