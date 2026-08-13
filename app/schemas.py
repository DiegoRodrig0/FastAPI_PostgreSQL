from datetime import date, time
from typing import Literal

from pydantic import BaseModel, ConfigDict


class EspecialidadeBase(BaseModel):
    nome: str

class EspecialidadeResponse(EspecialidadeBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class UnidadeBase(BaseModel):
    nome: str
    endereco: str
    telefone: str

class UnidadeResponse(UnidadeBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class EquipeBase(BaseModel):
    nome: str
    unidade_id: int

class EquipeResponse(EquipeBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class ProfissionalBase(BaseModel):
    nome: str
    cpf: str
    crm: str
    equipe_id: int
    especialidade_id: int

class ProfisionaisResponse(ProfissionalBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class ConsultaBase(BaseModel):
    paciente_id: int
    profissional_id: int
    horario_id: int
    data_consulta: date
    observacao: str | None = None

class ConsultaPorUnidade(BaseModel):
    paciente_nome: str
    profissional_nome: str
    horario_hora_inicio: time
    horario_hora_fim: time
    data_consulta: date
    observacao: str | None = None
class ConsultaResponse(ConsultaBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class GradeBase(BaseModel):
    profissional_id: int
    dia_semana: str

class GradeResponse(GradeBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class PacienteBase(BaseModel):
    nome: str
    cpf: str
    data_nascimento: date
    telefone: str

class PacienteResponse(PacienteBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class HorarioBase(BaseModel):
    grade_id: int
    hora_inicio: time
    hora_fim: time

class HorarioResponse(BaseModel):
    id: int
    model_config = ConfigDict(from_attributes=True)

class UsuarioBase(BaseModel):
    nome: str
    email: str
    perfil: Literal["ADMIN", "MEDICO", "RECEPCAO"]

class UsuarioCreate(UsuarioBase):
    senha: str

class UsuarioResponse(UsuarioBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class LoginRequest(BaseModel):
    email: str
    senha: str