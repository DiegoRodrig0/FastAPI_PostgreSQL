from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app import models, schemas
from app.dependencies import get_db
from app.security import criar_token, verificar_senha

router = APIRouter(
    prefix="/auth",
    tags=["Autenticação"]
)

@router.post("/login")
def login(
    dados: OAuth2PasswordRequestForm = Depends(),  # noqa: B008
    db: Session = Depends(get_db)  # noqa: B008
):
    usuario = (
        db.query(models.Usuario)
        .filter(models.Usuario.email == dados.username)
        .first()
    )

    if not usuario:
        raise HTTPException(
            status_code=401,
            detail="E-mail ou senha inválidos"
        )

    senha_correta = verificar_senha(
        dados.password,
        usuario.senha_hash
    )

    if not senha_correta:
        raise HTTPException(
            status_code=401,
            detail="E-mail ou senha inválidos"
        )

    token = criar_token({
        "sub": str(usuario.id),
        "perfil": usuario.perfil
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }