from sqlalchemy.orm import Session

from src.models import User
from src.schemas.user_dto import UserDTO


def create_user(user_dto: UserDTO, db: Session) -> User:
    user = User(**user_dto.model_dump())

    db.add(user)
    db.commit()
    db.refresh(user)

    return user