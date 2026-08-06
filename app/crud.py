from datetime import time

from sqlalchemy.orm import Session

from app.models import (
    Consulta,
    Equipe,
    Especialidade,
    Horario,
    Paciente,
    Profissional,
    Unidade_Funcional,
)


def listar_especialidades(db: Session):
    return db.query(Especialidade).all()

def listar_unidades(db: Session):
    return db.query(Unidade_Funcional).all()

def listar_profissional(db: Session):
    return db.query(Profissional).all()

def buscar_profissional_nome(db: Session, nome: str):
    return db.query(Profissional).filter(
        Profissional.nome.ilike(f"%{nome}%")
    ).all()

def listar_equipe(db: Session):
    return db.query(Equipe).all()

def listar_consulta(db: Session):
    return db.query(Consulta).all()

def buscar_consulta_unidade(db: Session, unidade_id: int):
    return (
        db.query(Consulta)
        .join(Profissional, Consulta.profissional_id == Profissional.id)
        .join(Equipe, Profissional.equipe_id == Equipe.id)
        .filter(Equipe.unidade_id == unidade_id)
        .all()
    )

def buscar_consulta_intervalo(db: Session, hora_inicio: time, hora_fim: time):
    return (
        db.query(Consulta)
        .join(Consulta.horario)
        .filter(Horario.hora_inicio == hora_inicio)
        .all()
    )


def listar_paciente(db: Session):
    return db.query(Paciente).all()
