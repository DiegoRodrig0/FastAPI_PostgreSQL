from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud, schemas
from app.dependencies import get_db

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuários"]
)

@router.post(
    "/",
    response_model=schemas.UsuarioResponse
)
def criar_usuario(
    usuario: schemas.UsuarioCreate,
    db: Session = Depends(get_db)  # noqa: B008
):
    return crud.criar_usuario(db, usuario)