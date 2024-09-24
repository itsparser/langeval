import logging
from typing import Any

from langchain_core.language_models import BaseChatModel
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, PromptTemplate
from langgraph.prebuilt import create_react_agent
from pydantic import BaseModel

from langval.error import EvalThreshold
from langval.eval.base import BaseEval
from langval.model import EvalMetric, Validation
from langval.prompt import LANGCHAIN_SYSTEM_PROMPT


class LangchainEval(BaseEval):
	"""
	Langchain evaluation class for evaluating the toxicity, accuracy, hallucination, and bias of language models.
	"""

	def __init__(self, llm: BaseChatModel, *, validation: Validation = None):
		super().__init__(validation=validation)
		self.llm = llm

	@property
	def node(self):
		prompt = PromptTemplate.from_template(LANGCHAIN_SYSTEM_PROMPT)
		llm = prompt | self.llm.with_structured_output(EvalMetric)
		return llm

	def eval(
		self,
		answer: Any,
		question: Any = None,
		expected_answer: Any = None,
		validation: Validation = None,
	) -> EvalMetric:
		"""
		Evaluates the toxicity, accuracy, hallucination, and bias of a language model.

		Args:
		    question (Any): The question to evaluate.
		    answer (Any): The answer to evaluate.
		    expected_answer (Any, optional): The expected answer. Defaults to None.
		    validation (Validation, optional): The validation to evaluate the model. Defaults to None.

		Returns:
		    EvalMetric: The evaluation metric.
		"""
		if not validation:
			validation = self.validation
		if question:
			question = f'question -->\n {question}\n'
		if expected_answer:
			expected_answer = f'Expected answer -->\n {expected_answer}\n'
		validation_result: dict | EvalMetric = self.node.invoke(
			{'question': question, 'answer': answer, 'expected_answer': expected_answer}
		)
		result, exact_match = validation.compare(validation_result)
		if exact_match:
			logging.warning(f'Following exact match found to be in Meet Expectation: {exact_match}')
		if result:
			raise EvalThreshold(result)
		return validation_result
