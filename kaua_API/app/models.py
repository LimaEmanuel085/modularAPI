from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId

# Para permitir que o Pydantic entenda o ObjectId do MongoDB
class PyObjectId(ObjectId):

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("ObjectId inválido")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

# Modelo base da tarefa armazenada no MongoDB
class TaskModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    title: str
    description: Optional[str] = None
    completed: bool = False
    user_id: str  # para saber de qual usuário é a tarefa

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }

# Modelo para criação de nova tarefa (sem _id e completed)
class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    user_id: str