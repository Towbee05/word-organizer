from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from datetime import datetime
from app.core.logging_config import setup_logging
from app.schema.response import ErrorResponse
from app.routes.routes import router
import logging 

setup_logging()

app = FastAPI()
logger = logging.getLogger("app")

@app.get("/")
def root():
    logger.info("root endpoint accessed")
    return {
        "status": "healthy",
        "message": "Hello world. Welcome to my Proof Reader."
    }

@app.get("/health")
def health():
    logger.info("health endpoint accessed")
    return {
        "status": "healthy and running...",
        "message": "Hello, world. I am currently running",
        "timestamp": datetime.now().strftime(f"%H:%M%p %d/%m/%Y").lower()
    }

@app.exception_handler(HTTPException)
async def override_default_exception(request, exec: HTTPException):
    return JSONResponse(status_code=exec.status_code, content=ErrorResponse(
        error="request_error", message=exec.detail
    ).model_dump())



app.include_router(router)