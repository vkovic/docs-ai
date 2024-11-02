from typing import Union

from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr, ValidationError

app = FastAPI()

@app.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {str(exc)} did something. There goes a rainbow..."},
    )

class UserDTO(BaseModel):
    username: str
    full_name: str
    email: EmailStr
    address: str = None

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

def get_full_name(first_name: str, last_name: str, age: Union[str, None] = None) -> str:
    full_name = first_name + 'a' + last_name + str(age)
    return full_name

@app.get("/")
def read_root():
    user_data = {
        "username": "john_doe",
        "full_name": "John Doe",
        "email": "johndoe@google.com"
    }

    user_invalid_data = {
        "username": "john_doe",
        "full_name": "John Doe",
        "email": "johnd.com"
    }

    try:
        # invalid_user_dto = UserDTO(**user_invalid_data)
        UserDTO(email="johnd.com", full_name="John Doe", username="john_doe")
    except ValidationError as e:
        return JSONResponse(
            status_code=404,
            content={"message": str(e)}
        )

    user_dto = UserDTO(**user_data)
    return user_dto.json()
    # return {"Hello": get_full_name("john", "doe")}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_price": item.price, "item_offer": item.is_offer}
