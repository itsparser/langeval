from enum import Enum

from pydantic import BaseModel, Field


class ModuleType(str, Enum):
    CLASS = "class"
    FUNCTION = "function"



class EvalModel(BaseModel):
    toxicity: float = Field(description="toxicity score", ge=0, le=1, decimal_places=2)
    accuracy: float = Field(description="accuracy score", ge=0, le=1, decimal_places=2)
    hallucination: float = Field(description="hallucination score", ge=0, le=1, decimal_places=2)
    bias: float = Field(description="bias score", ge=0, le=1, decimal_places=2)
    justification: str = Field(description="justification for the score")


class ModuleModel(BaseModel):
    name: str = Field(description="name of the module")
    type: str = Field(description="type of the module")
    metrics: EvalModel = Field(description="metrics of the module")