from abc import ABC, abstractmethod
from typing import Any, override

from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel

from langval.model import EvalMetric, ModuleModel, Validation
from langval.tools import arithemetic, comparison
from langval.utils import check_type


class BaseEval(ABC):
	"""
	Base class for all evaluations in langval
	"""

	registry = {}
	TOOLS = [arithemetic, comparison]

	def __init__(self, *args, **kwargs):
		self.validation = kwargs.get('validation') or Validation()

	@abstractmethod
	def eval(
		self, answer: Any, question: Any = None, expected_answer: Any = None
	) -> dict | BaseModel:
		"""
		Evaluates the model, Need to been override in all subclasses
		Args:
		    answer (Any): The answer to evaluate.
		    question (Any, optional): The question to evaluate. Defaults to None.
		    expected_answer (Any, optional): The expected answer. Defaults to None.

		Returns:
		    dict | BaseModel: The evaluation result.
		"""
		pass

	def compare(self, metric: EvalMetric, validation: Validation = None):
		"""
		Compares the metric with the validation
		Args:
			metric (EvalMetric): The metric to compare
			validation (Validation, optional): The validation to compare with. Defaults to None.

		Returns:
			bool: True if the metric is equal to the validation, False otherwise.
		"""
		if not validation:
			validation = self.validation
		result, exact_match = validation.compare(metric)
		return result, exact_match

	@classmethod
	def validate(cls, toxicity: float, accuracy: float, hallucination: float, bias: float):
		def decorator(_mod):
			_type = check_type(_mod)
			cls.registry[_type][_mod.__name__] = ModuleModel(
				name=_mod.__name__,
				type=_type,
				metrics=Validation(
					toxicity=toxicity, accuracy=accuracy, hallucination=hallucination, bias=bias
				),
			)

		return decorator

	@classmethod
	def question(cls, q: str = None):
		def decorator(func):
			setattr(func, 'question', q)
			return func

		return decorator
