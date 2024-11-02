from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

class User(declarative_base()):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, email={self.email})>"