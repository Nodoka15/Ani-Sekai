from fastapi import APIRouter, Path
from typing import Annotated
from pydantic import BaseModel
router = APIRouter()

@router.get("/")
async def read_root():
    return {"Hello":"World"}

@router.get("/{id}")
async def read_item(id: int, q : str | None):
    return {"id": id, "q":q} 