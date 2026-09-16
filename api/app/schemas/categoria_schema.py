from pydantic import ConfigDict, Field, BaseModel


class CategoriaCriar(BaseModel):
    nome: str = Field(min_length=2, max_length=60, description="Nome único da categoria")
    descricao: str | None = Field(default=None, max_length=255, description="Descrição optional")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "nome":"rede",
                "descricao": "Problems de conexão, Wi-Fi, VPN e cabeamento"
            }
        }
    )


class CategoriaEditar(BaseModel):
    nome: str = Field(min_length=2, max_length=60, description="Nome único da categoria")
    descricao: str | None = Field(default=None, max_length=255, description="Descrição optional")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "nome":"rede",
                "descricao": "Problems de conexão, Wi-Fi, VPN e cabeamento"
            }
        }
    )


class CategoriaResposta(BaseModel):
    id: int
    nome: str
    descricao: str | None

    model_config = ConfigDict(
        from_attributes = True
    )