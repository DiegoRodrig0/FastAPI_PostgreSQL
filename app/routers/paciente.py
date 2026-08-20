from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud, schemas
from app.dependencies import get_db, get_usuario_atual

router = APIRouter(
    prefix="/paciente",
    tags=["Paciente"]
)

@router.get(
    "/listar",
    response_model=list[schemas.PacienteResponse]
)
def listar(db: Session = Depends(get_db), usuario=Depends(get_usuario_atual)):  # noqa: B008
    return crud.listar_paciente(db)