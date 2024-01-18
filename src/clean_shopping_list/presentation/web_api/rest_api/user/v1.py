from fastapi import APIRouter

user_router = APIRouter()


@user_router.post('')
def create_user():
    return {
        'token': 'dfjskdfdf'
    }
