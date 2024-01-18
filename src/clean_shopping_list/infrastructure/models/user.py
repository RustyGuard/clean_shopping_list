from sqlalchemy.orm import Mapped, mapped_column

from src.clean_shopping_list.infrastructure.models.base import BaseSqlAlchemyModel


class User(BaseSqlAlchemyModel):
    email: Mapped[str] = mapped_column(primary_key=True)
    hashed_password: Mapped[str]
