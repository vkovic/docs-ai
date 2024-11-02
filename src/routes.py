from typing import Union

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from sqlalchemy.orm import Session

from .database import get_db
from .models.user import User
from .schemas.item import Item
from .schemas.user import User as UserDTO

router = APIRouter()


@router.get("/test")
def test(db: Session = Depends(get_db)):
    new_user = User(name="Alice", email="alice@example.com")
    db.add(new_user)
    db.commit()
    users = db.query(User).all()
    return {"users": users}


@router.get("/")
def read_root():
    user_data = {
        "username": "john_doe",
        "full_name": "John Doe",
        "email": "johndoe@google.com"
    }
    try:
        UserDTO(email="johnd.com", full_name="John Doe", username="john_doe")
    except ValidationError as e:
        return JSONResponse(
            status_code=404,
            content={"message": str(e)}
        )
    user_dto = UserDTO(**user_data)
    return user_dto.json()


@router.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@router.post("/items")
def create_item(item: Item):
    return item

