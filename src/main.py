from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from .database import engine
from .models.base import Base
from .routes import router

# Init app
app = FastAPI()

# Error handler
@app.exception_handler(Exception)
async def exception(request: Request, exc: Exception):
    return JSONResponse(
        status_code=400,
        content={
            "detail": str(exc),
            "url": str(request.url),
        }
    )

# Init db
Base.metadata.create_all(bind=engine)

# Routes
app.include_router(router)
