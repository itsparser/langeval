from langchain_openai import ChatOpenAI

import langeval
from langeval import TestCase
from langeval.eval import BaseEval
from langeval.eval.langchain import LangchainEval
from langeval.model import Validation

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

    @langeval.assess(model=llm, question="What is the capital of France?")
    def test_eval(self):
        return "paris"

    @langeval.assess("What is the capital of India?")
    def test_001(self):
        return "paris"

    @classmethod
    def tearDownClass(cls):
        del cls.model
