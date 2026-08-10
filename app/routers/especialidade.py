from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud, schemas
from app.dependencies import get_db, get_usuario_atual

router = APIRouter(
    prefix="/especialidades",
    tags=["Especialidades"]
)

@router.get(
    "/",
    response_model=list[schemas.EspecialidadeResponse]
)
def listar(db: Session = Depends(get_db), usuario=Depends(get_usuario_atual)):  # noqa: B008
    return crud.listar_especialidades(db)