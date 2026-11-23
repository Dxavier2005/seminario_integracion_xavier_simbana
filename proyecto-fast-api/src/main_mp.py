from fastapi import FastAPI
from pydantic import BaseModel
from routers.hello_world_mp import router
from routers.task_router_mp import inscripcion_router

app = FastAPI(title="Control de Cursos de Sacramentos")

app.include_router(router)
app.include_router(inscripcion_router)