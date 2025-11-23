from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db.database import create_table
from core.config import settings
import uvicorn 
from routes import user

create_table()

app = FastAPI(
    title="hatable",
    description="Frontend code generating app",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_headers=['*'],
    allow_methods=['*'],
)

app.include_router(user.router, prefix="/auth")

@app.get("/")
def root():
    return{"message": "Love this hatable code gen app."}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)