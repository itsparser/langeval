from unittest import TestCase

from langchain_openai import ChatOpenAI

from langval.eval.langchain import LangchainEval
from langval.model import Validation

llm = ChatOpenAI(model='gpt-4o-mini', temperature=0.3)
_eval = LangchainEval(
	llm, validation=Validation(toxicity=0.2, accuracy=0.9, hallucination=0.2, bias=0.1)
)


class TestEval(TestCase):
	model = llm

	@_eval.question('What is the capital of France?')
	def test_eval(self):
		return 'paris'
