from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession

from secao04.db.session import Session


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """
    Dependência para obter uma sessão assíncrona do banco de dados.
    """
    async with Session() as session:
        yield session
