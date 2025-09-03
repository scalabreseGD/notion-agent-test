from fastapi import APIRouter
from duckduckgo_search import DDGS

router = APIRouter()

@router.get("/search")
def search_ddg(query: str):
    with DDGS() as ddgs:
        results = ddgs.text(query)
        return results