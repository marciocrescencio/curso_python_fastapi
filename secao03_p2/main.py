from fastapi import FastAPI
from routes.curso_router import router as curso_router
from routes.usuario_router import router as usuario_router  

app = FastAPI(
    title="API de Cursos",
    description="API para gerenciar cursos",
    version="1.0.0",
    contact={
        "name": "Instituto Federal Catarinense",
        "email": "csi@ifc.edu.br"
    }
)

# Incluindo os routers
app.include_router(curso_router, tags=["cursos"])
app.include_router(usuario_router, tags=["usuarios"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8002, reload=True)