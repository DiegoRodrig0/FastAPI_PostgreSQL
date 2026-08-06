from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud, schemas
from app.dependencies import get_db

router = APIRouter(
    prefix="/paciente",
    tags=["Paciente"]
)

@router.get(
    "/",
    response_model=list[schemas.PacienteResponse]
)
def listar(db: Session = Depends(get_db)):  # noqa: B008
    return crud.listar_paciente(db)