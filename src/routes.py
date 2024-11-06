from typing import Union

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .database import get_db
from .models.item import Item
from .models.user import User
from .schemas.item_dto import ItemDTO
from .schemas.user_dto import UserDTO
from .services.create_user_service import create_user
from .services.ollama_chat_service import chat

router = APIRouter()


@router.get("/chat")
def test_ollama():
    return {"answer": chat()}


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
        "email": "johndoegoogle.com"
    }

    return UserDTO(**user_data)


@router.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@router.post("/items")
def create_item(item_dto: ItemDTO, db: Session = Depends(get_db)):
    item = Item(**item_dto.model_dump())

    db.add(item)
    db.commit()
    db.refresh(item)

    return {"success": True}


@router.post("/users")
def create_user(user_dto: UserDTO, db: Session = Depends(get_db)):
    return create_user(user_dto, db)
