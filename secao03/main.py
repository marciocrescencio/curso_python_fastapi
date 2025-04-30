from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from fastapi import Path
from models import Curso
from pydantic import ValidationError

app = FastAPI(title="API de Cursos",
    description="API para gerenciar cursos",
    version="1.0.0",
    contact={
        "name": "Instituto Federal Catarinense",
        "email": "csi@ifc.edu.br"})

cursos = {
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

@app.get("/cursos")
async def get_cursos():
    return cursos

@app.get("/cursos/{curso_id}")
async def get_curso(curso_id: int = Path(..., title="ID do curso", description="Deve ser maior ou igual a 1", ge=1)):
    try:
        curso = cursos[curso_id]
        return curso
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Curso não encontrado"
        )

## criar um novo curso
@app.post("/cursos", status_code=status.HTTP_201_CREATED)
async def create_curso(curso: Curso):    
    novo_id = len(cursos) + 1
    curso.id = novo_id
    if novo_id in cursos:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="ID já existe"
        )
    cursos[novo_id] = curso
    return cursos[novo_id]


@app.put("/cursos/{curso_id}")
async def update_curso(curso_id: int, curso: Curso):
    if curso_id not in cursos:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Curso não encontrado"
        )
    cursos[curso_id] = curso
    return cursos[curso_id]

@app.delete("/cursos/{curso_id}", status_code=status.HTTP_204_NO_CONTENT) 
async def delete_curso(curso_id: int):
    if curso_id not in cursos:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Curso não encontrado"
        )
    del cursos[curso_id]
    return None 

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)