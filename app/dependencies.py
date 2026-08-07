import jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app import models
from app.database import SessionLocal
from app.security import verificar_token

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)

def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()

def get_usuario_atual(
        token: str = Depends(oauth2_scheme),
        db: Session = Depends(get_db)  # noqa: B008
):
    try:
        payload = verificar_token(token)

    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=401,
            detail="Token inválido"
        )

    usuario_id = payload.get("sub")

    if usuario_id is None:
        raise HTTPException(
            status_code=401,
            detail="Token inválido"
        )

    usuario = (
        db.query(models.Usuario)
        .filter(models.Usuario.id == int(usuario_id))
        .first()
    )

    if usuario is None:
        raise HTTPException(
            status_code=401,
            detail="Usuário não encontrado"
        )

    return usuario