from fastapi import APIRouter
from app.api.v1.endpoints import tester

api_router = APIRouter()

api_router.include_router(tester.router, prefix="/tester", tags=["Tester"])