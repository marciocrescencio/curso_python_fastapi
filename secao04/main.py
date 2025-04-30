from fastapi import FastAPI
from secao04.core.configs import settings
from secao04.api.v1.routes import router as api_router

app = FastAPI(title="FastAPI Project")

app.include_router(api_router, prefix=settings.API_V1_STR)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("secao04.main:app", host="0.0.0.0", port=8001, reload=True)