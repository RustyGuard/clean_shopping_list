from typing import Iterator

from sqlalchemy.orm import Session
from starlette.requests import Request


async def session_maker(request: Request) -> Iterator[Session]:
    async with request.app.state.sessionmaker() as conn:
        yield conn

