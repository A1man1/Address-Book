from fastapi import APIRouter

from src.endpoints.v1.api_v1 import router as address_router

api_router = APIRouter()

api_router.include_router(address_router)