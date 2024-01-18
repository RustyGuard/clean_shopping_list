from datetime import timedelta

import sqlalchemy
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, SecretStr
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from src.clean_shopping_list.adapters.auth.hash import hash_password
from src.clean_shopping_list.adapters.auth.token import create_access_token
from src.clean_shopping_list.config import get_config
from src.clean_shopping_list.infrastructure.models import User
from src.clean_shopping_list.presentation.dependencies import session_maker

user_router = APIRouter()

config = get_config()

class UserLogin(BaseModel):
    email: str
    password: SecretStr


@user_router.post('')
async def create_user(
        form: UserLogin,
        session: AsyncSession = Depends(session_maker),
):
    hashed_password = hash_password(password=str(form.password), password_secret=config.PASSWORD_SECRET)
    user = User(
        email=form.email,
        hashed_password=hashed_password.decode(),
    )
    session.add(user)
    try:
        await session.commit()
    except IntegrityError:
        await session.rollback()
        raise HTTPException(status_code=400, detail='Пользователь с данным email уже существует')
    access_token = create_access_token(form.email, timedelta(minutes=30), config.JWT_SECRET)
    return {
        'token': access_token
    }
