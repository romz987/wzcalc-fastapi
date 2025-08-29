from fastapi import FastAPI
from src.check.router import router as check_router
from src.calc.router import router as calc_router

app = FastAPI()

# Регистрация endpoints check
app.include_router(check_router, prefix="/check", tags=["check-app"])
# Регистрация endpoints calc
app.include_router(calc_router, prefix="/api/v1", tags=["calcs"])
