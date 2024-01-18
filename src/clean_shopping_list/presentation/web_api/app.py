from fastapi import FastAPI

from src.clean_shopping_list.presentation.web_api.rest_api.shopping_list.v1 import shopping_list_router
from src.clean_shopping_list.presentation.web_api.rest_api.user.v1 import user_router


def get_application() -> FastAPI:
    app = FastAPI()
    app.include_router(shopping_list_router, prefix='/api/v1/shopping_list')
    app.include_router(user_router, prefix='/api/v1/user')
    return app
