from abc import abstractmethod, ABC
from typing import Any, override

from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel

from langval.model import Validation, ModuleModel
from langval.tools import arithemetic, comparison
from langval.utils import check_type


class BaseEval(ABC):
    """
    Base class for all evaluations in langval
    """
    registry={}
    TOOLS = [arithemetic, comparison]
    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    def eval(self, answer: Any, question: Any=None,  expected_answer: Any = None) ->  dict | BaseModel:
        pass

    @classmethod
    def validate(cls, toxicity: float, accuracy: float, hallucination: float, bias: float):
        def decorator(_mod):
            _type = check_type(_mod)
            cls.registry[_type][_mod.__name__] = ModuleModel(name=_mod.__name__, type=_type,
                                                             metrics=Validation(toxicity=toxicity, accuracy=accuracy,
                                                                                hallucination=hallucination, bias=bias))
        return decorator

    @classmethod
    def eval(cls, input_text: str):
        def decorator(func):
            setattr(func, 'eval_input', input_text)
            return func
        return decorator