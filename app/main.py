from fastapi import FastAPI

from app.routers import (
    consulta,
    equipe,
    especialidade,
    paciente,
    profissionais,
    unidade_funcional,
    usuario,
)

app = FastAPI()

app.include_router(especialidade.router)

app.include_router(unidade_funcional.router)

app.include_router(profissionais.router)

app.include_router(equipe.router)

app.include_router(consulta.router)

app.include_router(paciente.router)

app.include_router(usuario.router)