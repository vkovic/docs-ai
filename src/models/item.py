from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


class Item(declarative_base()):
    __tablename__ = "items"

    id = Column(Integer, primary_key=False)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    description = Column(String, nullable=True)

    def __repr__(self):
        return f"<Item(id={self.id}, name={self.name}, price={self.price}, description={self.description})>"
