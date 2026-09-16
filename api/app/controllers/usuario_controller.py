from fastapi import APIRouter, Depends

from app.dependencies.database import DbSession
from app.schemas.usuario_schema import UsuarioCriar, UsuarioEditar, UsuariosListar
from app.services.usuario_service import UsuarioService


router = APIRouter(prefix="/usuarios", tags=["Usuários"])

@router.post(
        "",
        summary="Cadastrar usuario",
        response_model=UsuariosListar
    )
def criar(dado: UsuarioCriar, db: DbSession):
    return UsuarioService(db).criar(dado)


@router.get(
        "",
        summary="Listar usuarios",
        response_model=list[UsuariosListar],
)
def listar(db: DbSession):
    return UsuarioService(db).listar()


@router.put("/{id}")
def editar(id: int, dado: UsuarioEditar, db: DbSession):
    return UsuarioService(db).editar(id, dado)


@router.get(
    "/{id}",
    summary="Consultar usuario por id",
    response_model=UsuariosListar
)
def consultar_por_id(id: int, db: DbSession):
    return UsuarioService(db).obter_por_id(id)


@router.delete(
    "/{id}",
    summary="Apagar usuario filtrando por id",
    response_model=UsuariosListar
)
def apagra(id: int, db: DbSession):
    return UsuarioService(db).apagar(id)

