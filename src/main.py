from fastapi import FastAPI
from src.check.router import router as check_router

app = FastAPI()

# Регистрация endpoints check
app.include_router(check_router, prefix="/check", tags=["check-app"])
