from fastapi import UploadFile, File, Response, status, HTTPException
from app.routes.routes import router
from app.core.config import settings
from app.schema.response import SuccessResponse
from app.core import get_storage
from pathlib import Path
import logging

logger = logging.getLogger("app")

@router.post('/upload', response_model=SuccessResponse, status_code=status.HTTP_202_ACCEPTED)
async def upload_docs(file: UploadFile= File(...)):
    file_content_type = file.content_type
    
    if not file_content_type in settings.ALLOWED_CONTENT_TYPES:
        logger.info(f"Unsupported file type submitted: {file_content_type}")
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_CONTENT, detail="Submitted file type not supported")
    
    storage = get_storage(settings.STORAGE_BACKEND, settings.STORAGE_UPLOAD_DIR)
    
    # save data to storage
    
    file_content = await file.read()
    await storage.save(f"{file.filename}", file_content)
    logger.info(f"file saved to storage: {file.filename}")

    return SuccessResponse(data= {
        "message": "hello, world",
        "content-type": file.content_type,
        "name": file.filename
    })