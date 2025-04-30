from fastapi import APIRouter


router = APIRouter(
    prefix="/usuarios",
    tags=["usuarios"]
)

@router.get("/api/v1/usuarios")
async def get_usuarios():
    return {
        1: {        
            "nome": "João",
            "email": "joao@mail.com",
            "senha": "123456"
        },
        2: {        
            "nome": "Maria",
            "email": "maria@mail.com",
            "senha": "123456"
        }, 
    }      