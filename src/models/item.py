from sqlalchemy import Column, Integer, String

from .base import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    description = Column(String, nullable=True)

    def __repr__(self):
        return f"<Item(id={self.id}, name={self.name}, price={self.price}, description={self.description})>"
