import asyncio
from secao04.db.base import Base
from secao04.db.session import engine

# 👇 IMPORTAÇÃO explícita dos modelos
from secao04.models import user  # isso registra o modelo User no Base.metadata

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    asyncio.run(create_tables())
