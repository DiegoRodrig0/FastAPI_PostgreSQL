from sqlalchemy import Column, Date, ForeignKey, Integer, String, Text, Time
from sqlalchemy.orm import relationship

from app.database import Base


class Especialidade(Base):

    __tablename__ = "especialidade"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(150), nullable=False)
    profissional = relationship(
        "Profissional",
        back_populates="especialidade"
    )

class Unidade_Funcional(Base):

    __tablename__ = "unidade_funcional"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(150), nullable=False)
    endereco = Column(String(150))
    telefone = Column(String(150))
    equipes = relationship(
        "Equipe",
        back_populates="unidade_funcional"
    )

class Equipe(Base):

    __tablename__ = "equipe"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(150), nullable=False)
    unidade_id = Column(
            Integer,
            ForeignKey("unidade_funcional.id")
        )
    unidade_funcional = relationship(
        "Unidade_Funcional",
        back_populates="equipes"
    )

    profissional = relationship(
        "Profissional",
        back_populates="equipe"
    )

class Profissional(Base):

    __tablename__ = "profissional"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    cpf = Column(String, unique=True)
    crm = Column(String(150))
    equipe_id = Column(
        Integer,
        ForeignKey("equipe.id")
    )
    especialidade_id = Column(
        Integer,
        ForeignKey("especialidade.id")
    )
    equipe = relationship(
        "Equipe",
        back_populates="profissional"
    )
    especialidade = relationship(
        "Especialidade",
        back_populates="profissional"
    )
    consulta = relationship(
            "Consulta",
            back_populates="profissional"
        )
    grade = relationship(
            "Grade",
            back_populates="profissional"
        )

class Consulta(Base):

    __tablename__ = "consulta"
    id = Column(Integer, primary_key=True, index=True)
    paciente_id = Column(
        Integer,
        ForeignKey("paciente.id")
    )
    profissional_id = Column(
        Integer,
        ForeignKey("profissional.id")
    )
    horario_id = Column(
        Integer,
        ForeignKey("horario.id")
    )
    data_consulta = Column(Date, nullable=False)
    observacao = Column(Text)
    paciente = relationship(
            "Paciente",
            back_populates="consulta"
        )
    profissional = relationship(
            "Profissional",
            back_populates="consulta"
        )
    horario = relationship(
            "Horario",
            back_populates="consulta"
        )

class Grade(Base):

    __tablename__ = "grade"
    id = Column(Integer, primary_key=True, index=True)
    profissional_id = Column(
        Integer,
        ForeignKey("profissional.id")
    )
    dia_semana = Column(String)
    profissional = relationship(
            "Profissional",
            back_populates="grade"
        )
    horario = relationship(
            "Horario",
            back_populates="grade"
        )

class Paciente(Base):

    __tablename__ = "paciente"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(150), nullable=False)
    cpf = Column(String(150), unique=True)
    data_nascimento = Column(Date)
    telefone = Column(String)
    consulta = relationship(
            "Consulta",
            back_populates="paciente"
        )

class Horario(Base):

    __tablename__ = "horario"
    id = Column(Integer, primary_key=True, index=True)
    grade_id = Column(
        Integer,
        ForeignKey("grade.id")
    )
    hora_inicio = Column(Time)
    hora_fim = Column(Time)
    consulta = relationship(
            "Consulta",
            back_populates="horario"
        )
    grade = relationship(
            "Grade",
            back_populates="horario"
        )

class Usuario(Base):

    __tablename__ = "usuario"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(150), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    senha_hash = Column(String(255), nullable=False)
    perfil = Column(String(30), nullable=False)