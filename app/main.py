from fastapi import FastAPI
from app.routes import files

app = FastAPI(title="CS COMPLIER AZURE")

app.include_router(files.router)