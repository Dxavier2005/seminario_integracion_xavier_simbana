# app/routers/paso1_inscripcion_create_body.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

inscripcion_router = APIRouter()

class InscripcionCreate(BaseModel):
    """Lo que el cliente envía para crear una inscripción. Sin id: lo asigna el servidor."""
    nombre: str = Field(min_length=3, max_length=100)
    observaciones: str | None = None
    sacramento: str = "Primera Comunión"
    documentos: list[str] = Field(default_factory=list)


class InscripcionRead(BaseModel):
    """Lo que el servidor expone al leer una inscripción. Incluye campos calculados por el servidor."""
    id: int
    nombre: str
    observaciones: str | None
    sacramento: str
    documentos: list[str]
    curso_completado: bool


class InscripcionUpdate(BaseModel):
    """Lo que el cliente envía para actualizar. TODOS los campos son opcionales."""
    nombre: str | None = Field(default=None, min_length=3, max_length=100)
    observaciones: str | None = None
    sacramento: str | None = None
    documentos: list[str] | None = None
    curso_completado: bool | None = None


INSCRIPCIONES: list[dict] = [
    {"id": 1, "nombre": "María Fernanda López", "observaciones": None, "sacramento": "Primera Comunión", "documentos": ["partida de bautismo", "cédula"], "curso_completado": False},
    {"id": 2, "nombre": "Juan Pablo Torres", "observaciones": None, "sacramento": "Confirmación", "documentos": ["partida de bautismo", "certificado de comunión"], "curso_completado": False},
]
SIGUIENTE_ID = len(INSCRIPCIONES) + 1


@inscripcion_router.post("/inscripciones", response_model=InscripcionRead)
def create_inscripcion(inscripcion: InscripcionCreate) -> dict:
    global SIGUIENTE_ID
    nueva_inscripcion = {
        "id": SIGUIENTE_ID,
        "curso_completado": False,
        "notas_internas": "creado desde la API",
        **inscripcion.model_dump(),
    }
    INSCRIPCIONES.append(nueva_inscripcion)
    SIGUIENTE_ID += 1
    return nueva_inscripcion


@inscripcion_router.get("/inscripciones", response_model=list[InscripcionRead])
def list_inscripciones() -> list[dict]:
    return INSCRIPCIONES


@inscripcion_router.patch("/inscripciones/{inscripcion_id}")
def update_inscripcion(inscripcion_id: int, update: InscripcionUpdate) -> dict:
    for inscripcion in INSCRIPCIONES:
        if inscripcion["id"] == inscripcion_id:
            changes = update.model_dump(exclude_unset=True)
            inscripcion.update(changes)
            return inscripcion
    return {"error": "Inscripción no encontrada"}

@inscripcion_router.post("/inscripciones/from-model")
def create_from_model(inscripcion: InscripcionCreate) -> dict:
    # model_dump(): instancia de Pydantic -> dict plano de Python
    data = inscripcion.model_dump()
    nueva_inscripcion = {"id": len(INSCRIPCIONES) + 1, "curso_completado": False, **data}
    INSCRIPCIONES.append(nueva_inscripcion)

    # model_validate(): dict de Python -> instancia validada de Pydantic
    validated = InscripcionRead.model_validate(nueva_inscripcion)
    return validated.model_dump()

@inscripcion_router.get("/inscripciones/{inscripcion_id}/raw-vs-validated")
def compare_raw_validated(inscripcion_id: int) -> dict:
    raw = next((i for i in INSCRIPCIONES if i["id"] == inscripcion_id), None)
    if raw is None:
        return {"error": "no encontrada"}

    # model_validate lanza una excepción si el dict no cumple el schema de InscripcionRead
    validated = InscripcionRead.model_validate(raw)

    return {
        "raw_dict": raw,
        "validated_model_dump": validated.model_dump(),
        "validated_model_dump_json": validated.model_dump_json(),
    }

@inscripcion_router.delete("/inscripciones/{inscripcion_id}")
def delete_inscripcion(inscripcion_id: int) -> dict:
    for index, inscripcion in enumerate(INSCRIPCIONES):
        if inscripcion["id"] == inscripcion_id:
            inscripcion_eliminada = INSCRIPCIONES.pop(index)

            return {
                "message": "Inscripción eliminada correctamente",
                "inscripcion_eliminada": inscripcion_eliminada
            }

    raise HTTPException(
        status_code=404,
        detail="Inscripción no encontrada"
    )

@inscripcion_router.get("/inscripciones/{inscripcion_id}", response_model=InscripcionRead)
def get_inscripcion_by_id(inscripcion_id: int) -> dict:
    for inscripcion in INSCRIPCIONES:
        if inscripcion["id"] ==