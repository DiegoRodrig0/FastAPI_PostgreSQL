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
    Usuario,
)
from app.security import gerar_hash


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
        db.query(
            Paciente.nome.label("paciente_nome"),
            Profissional.nome.label("profissional_nome"),
            Horario.hora_inicio.label("horario_hora_inicio"),
            Horario.hora_fim.label("horario_hora_fim"),
            Consulta.data_consulta,
            Consulta.observacao
        )
        .join(Paciente, Consulta.paciente_id == Paciente.id)
        .join(Profissional, Consulta.profissional_id == Profissional.id)
        .join(Horario, Consulta.horario_id == Horario.id)
        .join(Equipe, Profissional.equipe_id == Equipe.id)
        .filter(Equipe.unidade_id == unidade_id)
        .all()
    )

def buscar_consulta_intervalo(db: Session, hora_inicio: time, hora_fim: time):
    return (
        db.query(
                    Paciente.nome.label("paciente_nome"),
                    Profissional.nome.label("profissional_nome"),
                    Horario.hora_inicio.label("horario_hora_inicio"),
                    Horario.hora_fim.label("horario_hora_fim"),
                    Consulta.data_consulta,
                    Consulta.observacao
                )
                .join(Paciente, Consulta.paciente_id == Paciente.id)
                .join(Profissional, Consulta.profissional_id == Profissional.id)
                .join(Horario, Consulta.horario_id == Horario.id)
                .join(Equipe, Profissional.equipe_id == Equipe.id)
                .filter(Horario.hora_inicio == hora_inicio)
                .all()
    )

def listar_paciente(db: Session):
    return db.query(Paciente).all()

def criar_usuario(db: Session, usuario):
    senha_hash = gerar_hash(usuario.senha)

    novo_usuario = Usuario(
        nome=usuario.nome,
        email=usuario.email,
        senha_hash=senha_hash,
        perfil=usuario.perfil
    )

    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)

    return novo_usuario

