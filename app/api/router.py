from fastapi import APIRouter
from .currency_converter.views import router as currency_converter_router

router = APIRouter()

router.include_router(currency_converter_router, prefix='/convert', tags=['product'])