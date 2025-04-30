from typing import Optional
from pydantic import BaseModel, field_validator, ValidationError

class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int    
    horas: int

   
    @field_validator("titulo")
    @classmethod
    def validar_titulo(cls, v):
        if len(v) < 5:
            raise ValueError("O título deve ter pelo menos 5 caracteres")
        return v

    @field_validator("aulas")
    @classmethod
    def validar_aulas(cls, v):
        if v < 1:
            raise ValueError("O número de aulas deve ser maior que 0")
        return v

    @field_validator("horas")
    @classmethod
    def validar_horas(cls, v):
        if v < 1:
            raise ValueError("O número de horas deve ser maior que 0")
        return v

