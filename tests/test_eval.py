from langchain_openai import ChatOpenAI

import langval
from langval import TestCase
from langval.eval import BaseEval
from langval.eval.langchain import LangchainEval
from langval.model import Validation

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)
_eval = LangchainEval(
    llm, validation=Validation(toxicity=0.2, accuracy=0.9, hallucination=0.2, bias=0.1)
)


class TestEval(TestCase):
    @property
    def evaluator(self) -> BaseEval:
        return _eval

    @classmethod
    def setUpClass(cls) -> None:
        cls.model = llm
        super().setUpClass()

    @langval.assess(model=llm, question="What is the capital of France?")
    def test_eval(self):
        return "paris"

    @langval.assess("What is the capital of India?")
    def test_001(self):
        return "paris"

    @classmethod
    def tearDownClass(cls):
        del cls.model
