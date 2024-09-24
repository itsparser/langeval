from unittest import TestCase

from langchain_openai import ChatOpenAI
from openai import api_key

from langval.eval.langchain import LangchainEval
from langval.model import Validation

llm = ChatOpenAI(model='gpt-4o-mini', temperature=0.3)
_eval = LangchainEval(
	llm, validation=Validation(toxicity=0.2, accuracy=0.9, hallucination=0.2, bias=0.1)
)


class TestEval(TestCase):
	# @evalva.validate(toxicity=0.5, accuracy=0.8, hallucination=0.2, bias=0.1)
	def test_eval(self):
		result = _eval.eval(question='Hello, how are you?', answer='Hello, I am fine.')
		print(result)
