import os
from pydantic.v1 import BaseSettings 


class Settings(BaseSettings):
    """
    Configurações para o projeto.
    """
    # Configurações do banco de dados
    API_V1_STR: str = "/api/v1"
    DB_URL: str



    # class Config:        
    #     env_file = ".env" 
    class Config:
        env_file = os.path.join(os.path.dirname(__file__), "..", ".env") # construindo um caminho para o arquivo .env que está na raiz do projeto
        env_file_encoding = 'utf-8'

settings = Settings() 