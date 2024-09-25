import unittest
from abc import abstractmethod

from .eval import BaseEval


class TestCase(unittest.TestCase):
    @property
    @abstractmethod
    def evaluator(self) -> BaseEval: ...

    @classmethod
    def setUpClass(cls) -> None:
        cls.result = {}

    def main(self):
        self.assertEqual(1, 1)
