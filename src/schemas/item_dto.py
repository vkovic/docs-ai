from pydantic import BaseModel


class ItemDTO(BaseModel):
    name: str
    price: float
    description: str = None
