from fastapi import APIRouter


router = APIRouter(
    prefix="/cursos",
    tags=["cursos"]
)

@router.get("/api/v1/cursos")
async def get_cursos():
    return {
        1: {        
            "titulo": "Aprendendo Python",
            "aulas": 115,
            "horas": 60
        },
        2: {        
            "titulo": "Aprendendo Java",
            "aulas": 85,
            "horas": 50
        },
        3: {        
            "titulo": "Aprendendo JavaScript",
            "aulas": 95,
            "horas": 40
        },
    }