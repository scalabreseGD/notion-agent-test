from fastapi import FastAPI
from app.api.endpoints import search

app = FastAPI()

app.include_router(search.router, prefix="/api/v1")