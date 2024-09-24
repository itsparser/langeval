# langval

langval is a language model evaluation tool for evaluating the toxicity, accuracy, hallucination, and bias of language
models.

## Installation

```bash
pip install langval
```

## Usage

```python
from unittest import TestCase

from langchain_openai import ChatOpenAI

from langval.eval.langchain import LangchainEval
from langval.model import Validation

llm = ChatOpenAI(model='gpt-4o-mini', temperature=0.3)
langeval = LangchainEval(
    llm, validation=Validation(toxicity=0.2, accuracy=0.9, hallucination=0.2, bias=0.1)
)


class TestEval(TestCase):
    model = llm

    @langeval.question('What is the capital of France?')
    def test_eval(self):
        return 'paris'

```

## Contributing

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) for more information.

## License

langval is licensed under the [MIT License](LICENSE).   
