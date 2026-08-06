from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud, schemas
from app.dependencies import get_db

router = APIRouter(
    prefix="/profissional",
    tags=["Profissional"]
)

@router.get(
    "/",
    response_model=list[schemas.ProfisionaisResponse]
)
def listar(db: Session = Depends(get_db)):  # noqa: B008
    return crud.listar_profissional(db)

@router.get("/buscar/{nome}", response_model=list[schemas.ProfisionaisResponse])
def buscar_por_nome(nome: str, db: Session = Depends(get_db)):  # noqa: B008
    return crud.buscar_profissional_nome(db, nome)