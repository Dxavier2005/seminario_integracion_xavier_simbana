from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Mensaje(BaseModel):
    texto: str
    prioridad: int = 1
    campo_interno: str

@router.get("/")
def read_root() -> dict[str, str]:
    return {"mensaje": "Hola desde FastAPI + uv",
            "autor": "Dario Simbaña",
            "version": "0.1.0"}

@router.get("/catequista")
def endpoint_catequista() -> Mensaje:
    return Mensaje(texto="Bienvenido al curso de Primera Comunión", campo_interno="desde el endpoint catequista")

@router.get("/catequizando", response_model=Mensaje)
def endpoint_catequizando():
    return {"texto": "Hola María Fernanda López",
            "prioridad": 5,
            "campo_interno": "imprime desde endpoint catequizando"}

@router.get("/campo-extra", response_model=Mensaje)
def endpoint_campo_extra():
    return {"texto": "Hola María Fernanda López",
            "prioridad": 5,
            "campo_interno": "si debe salir incluido en el modelo",
            "campo_extra": "no deberia salir"}