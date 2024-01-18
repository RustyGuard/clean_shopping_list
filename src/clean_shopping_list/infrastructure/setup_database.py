from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession, AsyncEngine

from src.clean_shopping_list.config import get_config

config = get_config()


def setup_database() -> tuple[AsyncEngine, async_sessionmaker[AsyncSession]]:
    engine = create_async_engine(str(config.DATABASE_URI), echo=False, pool_pre_ping=True)
    async_session_maker = async_sessionmaker(
        engine, expire_on_commit=False, autocommit=False, autoflush=False
    )
    return engine, async_session_maker
