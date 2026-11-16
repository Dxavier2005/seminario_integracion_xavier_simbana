from fastapi import APIRouter, FastAPI
from pydantic import BaseModel

router = APIRouter()

class Mensaje(BaseModel):
    texto: str
    prioridad: int = 1
    campo_interno: str = "Este campo no debería salir en la respuesta"
    
@router.get("/")
def read_root() -> dict[str, str]:
    return {"mensaje": "Hola desde FastAPI + uv,",
            "autor": "Dario Simbaña",
            
            }

@router.get("/Dario")
def endpoint_dario() -> Mensaje:
    return Mensaje(texto="Hola, desde Dario", prioridad=5, campo_interno="desde dario link")


@router.get("/Simbana", response_model=Mensaje)
def endpoint_Simbana():
    return {"texto": "Hola Dario", "prioridad": 5, "campo_interno": "no debería salir"}

@router.get("/campo-extra", response_model=Mensaje)
def endpoint_campo_extra():
    return {
        "texto": "Hola Dario",
        "prioridad": 5,
        "campo_interno": "no debería salir",
        "campo_extra": "Este campo no está definido en el modelo"
    }