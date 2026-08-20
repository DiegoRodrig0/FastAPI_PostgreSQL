from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud, schemas
from app.dependencies import get_db, get_usuario_atual

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuários"]
)

@router.post(
    "/criar",
    response_model=schemas.UsuarioResponse
)
def criar_usuario(
    usuario: schemas.UsuarioCreate,
    db: Session = Depends(get_db), usuarios=Depends(get_usuario_atual)  # noqa: B008
):
    return crud.criar_usuario(db, usuario)