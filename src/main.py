from fastapi import FastAPI
from src.excel import router

app = FastAPI()

app.include_router(router=router.router, prefix='/excel', tags=['excel'])

@app.get("/")
async def root():
    return {"message": "Hello World"}