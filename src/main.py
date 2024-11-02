from fastapi import FastAPI

from .database import engine
from .routes import router
from .models.base import Base

# Init app
app = FastAPI()

# Init db
Base.metadata.create_all(bind=engine)

# Routes
app.include_router(router)
