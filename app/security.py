import os

import jwt
from dotenv import load_dotenv
from pwdlib import PasswordHash

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

password_hash = PasswordHash.recommended()

def gerar_hash(senha: str):
    return password_hash.hash(senha)

def verificar_senha(senha: str, senha_hash: str):
    return password_hash.verify(senha, senha_hash)

def criar_token(data: dict):
    return jwt.encode(
        data,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

def verificar_token(token: str):
    return jwt.decode(
        token,
        SECRET_KEY,
        algorithms=[ALGORITHM]
    )