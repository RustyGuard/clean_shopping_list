from datetime import datetime, timedelta

from jose import jwt


def create_access_token(user_email: str, expires: timedelta, secret: str):
    algorithm = "HS256"
    to_encode = {"sub": user_email}
    expire = datetime.utcnow() + expires
    to_encode["exp"] = expire
    return jwt.encode(
        to_encode, secret, algorithm=algorithm,
    )
