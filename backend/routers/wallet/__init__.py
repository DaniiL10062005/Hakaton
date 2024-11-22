from fastapi import APIRouter

from .category import category_router
from .transaction import transaction_router

router = APIRouter()

router.include_router(category_router)
router.include_router(transaction_router)