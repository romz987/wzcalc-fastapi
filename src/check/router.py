from fastapi import APIRouter
from .schemas import UserInfo

router = APIRouter()


@router.get("/")
def read_root():
    return {"status": "up"}


@router.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


@router.post("/signup")
def register_user(payload: UserInfo):
    return {"user_name": payload.name, "user_email": payload.email}
