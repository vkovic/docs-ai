from fastapi import FastAPI

from .database import engine
from .exception_handler import exception_handler
from .models.base import Base
from .routes import router

# Init app
app = FastAPI()

# Init db
Base.metadata.create_all(bind=engine)

# Exception handler
app.add_exception_handler(Exception, exception_handler)

# Routes
app.include_router(router)