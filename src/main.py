from fastapi import FastAPI
from src.calc.router import router as calc_router

app = FastAPI()

# Регистрация endpoints calc
app.include_router(calc_router, prefix="/api/v1", tags=["calcs"])
