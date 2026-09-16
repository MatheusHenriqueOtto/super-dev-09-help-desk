from fastapi.routing import APIRouter
from app.dependencies.database import DbSession
from app.schemas.categoria_schema import CategoriaCriar, CategoriaEditar, CategoriaResposta
from app.services.categoria_service import CategoriaService

router = APIRouter(prefix="/categoria", tags=["Categorias"])

@router.get(
    "",
    summary="Lista de Categorias",
    response_model=list[CategoriaResposta]
)
def listar(db: DbSession):
    return CategoriaService(db).listar()

@router.get(
    "/{id}",
    summary="Obtem o id por categoria",
    response_model=CategoriaResposta
)
def consultar_por_id(id: int, db: DbSession):
    return CategoriaService(db).obter_por_id(id)


@router.post(
    "",
    summary="Cadastrar uma categoria",
    response_model=CategoriaResposta
)
def criar(dado: CategoriaCriar, db: DbSession):
    return CategoriaService(db).criar(dado)


@router.put(
    "/{id}",
    summary="Editar uma categoria",
    response_model=CategoriaResposta
)
def editar(id: int, db: DbSession, dado: CategoriaEditar):
    return CategoriaService(db).editar(id, dado)


@router.delete(
    "/{id}",
    summary="Apagar categori filtrando por id",
    #response_model=CategoriaResposta
)
def apagra(id: int, db: DbSession):
    return CategoriaService(db).apagar(id)