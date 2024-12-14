from fastapi import FastAPI
from app.api.routes import router as auth_router
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME) 

app.include_router(auth_router, prefix="/auth", tags=["auth"])
#from app.middleware import init_middlewares
#init_middlewares(app)

@app.get("/health")
def health_check():
    return {"status": "ok"}