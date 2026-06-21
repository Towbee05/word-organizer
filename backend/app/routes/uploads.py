from app.routes.routes import router

@router.post('/upload')
async def upload_docs():
    return {
        "message": "hello, world"
    }