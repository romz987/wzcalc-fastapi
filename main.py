from typing import Union

from fastapi import FastAPI

from pydantic import BaseModel


class UserInfo(BaseModel):
    name: str
    email: str


app = FastAPI()


@app.get("/")
def read_root():
    return {"Answer": "It works!"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/signup")
def register_user(payload: UserInfo):
    return {"user_name": payload.name, "user_email": payload.email}
