from fastapi import APIRouter

from src.clean_shopping_list.config import get_config

shopping_list_router = APIRouter()

config = get_config()


@shopping_list_router.get("/own")
def read_own_shopping_list():
    return {
        'items': [
            'apples',
            'bananas'
        ]
    }
