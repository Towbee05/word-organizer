from fastapi import FastAPI, APIRouter
from datetime import datetime
from app.routes.routes import router
import logging 

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

app.include_router(router)