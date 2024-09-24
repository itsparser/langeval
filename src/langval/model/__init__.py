from enum import Enum

from pydantic import BaseModel, Field


class ModuleType(str, Enum):
	CLASS = 'class'
	FUNCTION = 'function'


class Validation(BaseModel):
	toxicity: float = Field(description='toxicity score', ge=0, le=1, default=0.2)
	accuracy: float = Field(description='accuracy score', ge=0, le=1, default=0.9)
	hallucination: float = Field(description='hallucination score', ge=0, le=1, default=0.2)
	bias: float = Field(description='bias score', ge=0, le=1, default=0.1)


class EvalMetric(Validation):
	toxicity: float = Field(description='toxicity score', ge=0, le=1)
	accuracy: float = Field(description='accuracy score', ge=0, le=1)
	hallucination: float = Field(description='hallucination score', ge=0, le=1)
	bias: float = Field(description='bias score', ge=0, le=1)
	justification: str = Field(description='justification for the score')


class ModuleModel(BaseModel):
	name: str = Field(description='name of the module')
	type: str = Field(description='type of the module')
	metrics: EvalMetric = Field(description='metrics of the module')
