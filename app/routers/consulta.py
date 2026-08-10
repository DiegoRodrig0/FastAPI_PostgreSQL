from datetime import time

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud, schemas
from app.dependencies import get_db, get_usuario_atual

router = APIRouter(
    prefix="/consulta",
    tags=["Consulta"]
)

@router.get(
    "/",
    response_model=list[schemas.ConsultaResponse]
)
def listar(db: Session = Depends(get_db), usuario=Depends(get_usuario_atual)):  # noqa: B008
    return crud.listar_consulta(db)

@router.get("/buscar", response_model=list[schemas.ConsultaResponse])
def buscar_por_id(unidade_id: int, db: Session = Depends(get_db), usuario=Depends(get_usuario_atual)):  # noqa: B008
    return crud.buscar_consulta_unidade(db, unidade_id)

@router.get("/intervalo", response_model=list[schemas.ConsultaResponse])
def buscar_intervalo(hora_inicio: time, hora_fim: time, db: Session = Depends(get_db), usuario=Depends(get_usuario_atual)):  # noqa: B008
    return crud.buscar_consulta_intervalo(db, hora_inicio, hora_fim)