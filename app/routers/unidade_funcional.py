from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud, schemas
from app.dependencies import get_db

router = APIRouter(
    prefix="/unidades",
    tags=["Unidades"]
)

@router.get(
    "/",
    response_model=list[schemas.UnidadeResponse]
)
def listar(db: Session = Depends(get_db)):  # noqa: B008
    return crud.listar_unidades(db)
