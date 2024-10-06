from pydantic import BaseModel

class SchemaRestaurante(BaseModel):
    nome: str
    categoria: str

class SchemaRestauranteAlternarStatus(BaseModel):
    id: int

class SchemaRestauranteAvaliar(BaseModel):
    id: int
    nota: float

class SchemaRestauranteDeletar(BaseModel):
    id: int