from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from secao04.core.deps import get_session 
from secao04.models.user import User
from secao04.schemas.user_schema import UserCreate, UserRead

router = APIRouter()

@router.get("/ping")
async def ping():
    return {"msg": "pong"}

@router.get("/users", response_model=list[UserRead])  # 👈 define o schema de resposta
async def list_users(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(User))
    users = result.scalars().all()
    return users  # 👈 FastAPI vai converter para UserRead automaticamente

@router.post("/users", response_model=UserRead)  # 👈 define entrada/saída com schemas
async def create_user(user: UserCreate, session: AsyncSession = Depends(get_session)):
    new_user = User(**user.model_dump())  # cria instância ORM a partir do schema
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return new_user