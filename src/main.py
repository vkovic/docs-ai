from fastapi import FastAPI
from .database import engine
from .models.user import User
from .routes import router as api_router

app = FastAPI()

User.metadata.create_all(bind=engine)


app.include_router(api_router)