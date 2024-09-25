# 🧧 Langval

⚡ 🧠 Agentic LLM Evaluation Tool context-aware assessment applications ⚡

[![PyPI version](https://badge.fury.io/py/langval.svg)](https://badge.fury.io/py/langval)
[![Release Notes](https://img.shields.io/github/release/itsparser/langval?style=flat-square)](https://github.com/langchain-ai/langchain/releases)
[![CI](https://github.com/itsparser/langval/actions/workflows/build.yml/badge.svg)](https://github.com/itsparser/langval/actions/workflows/build.yml)
[![PyPI - License](https://img.shields.io/pypi/l/langchain-core?style=flat-square)](https://opensource.org/licenses/MIT)
[![GitHub star chart](https://img.shields.io/github/stars/itsparser/langval?style=flat-square)](https://star-history.com/#itsparser/langval)
[![Open Issues](https://img.shields.io/github/issues-raw/itsparser/langval?style=flat-square)](https://github.com/itsparser/langval/issues)

## 📋 About

**Langval** is a powerful and flexible language model evaluation tool designed for easy integration and comprehensive
assessment. Built on modern Python frameworks, Langval provides a robust platform for evaluating the performance of
language models across multiple critical dimensions.

With Langval, you can easily assess the toxicity, accuracy, hallucination, and bias of language models, ensuring that
your evaluations are comprehensive and reliable. Whether you're evaluating a chatbot, a language model, or any other
application, Langval offers a robust and flexible solution for evaluating the performance of your models.

## 📖 Documentation

For comprehensive documentation, please refer to the [Langval Documentation](https://langval.readthedocs.io/en/latest/).

## 📦 Installation

To install Langval, simply run the following command:

```bash
pip install langval
```

## 🚀 Quick Start

Langval is designed to be easy to use and integrate into your existing Python projects.
Similar to unit testing, Langval provides a simple and intuitive way to evaluate the performance of your language
models.
allows you to integrate Langval into your existing Python projects, making it easy to use and integrate into your
existing Python projects.

## Usage

Here's a basic example of how to use Langval:

```python
from langchain_openai import ChatOpenAI
import langval
from langval import TestCase
from langval.eval import BaseEval
from langval.eval.langchain import LangchainEval
from langval.model import Validation

# Initialize the language model
llm = ChatOpenAI(model="gpt-4-mini", temperature=0.3)

# Set up the evaluation
_eval = LangchainEval(
    llm,
    validation=Validation(toxicity=0.2, accuracy=0.9, hallucination=0.2, bias=0.1)
)


# Define test cases
class TestEval(TestCase):
    @property
    def eval(self) -> BaseEval:
        return _eval

    @classmethod
    def setUpClass(cls) -> None:
        cls.model = llm

    @langval.assess(model=llm, question="What is the capital of France?")
    def test_eval(self):
        return "Paris"

    @langval.assess("What is the capital of India?")
    def test_001(self):
        return "New Delhi"

    @classmethod
    def tearDownClass(cls):
        del cls.model
```

## Features

- **Multi-dimensional Evaluation**: Assess language models on toxicity, accuracy, hallucination, and bias.
- **Flexible Integration**: Works seamlessly with popular language model libraries like LangChain.
- **Customizable Thresholds**: Set your own thresholds for each evaluation dimension.
- **Easy-to-use Decorators**: Simplify the process of creating and running test cases.

## Configuration

Langval allows you to configure the evaluation criteria using the `Validation` class. You can set thresholds for:

- Toxicity
- Accuracy
- Hallucination
- Bias

Adjust these values according to your specific requirements.

## Examples

### Basic Evaluation

```python
@langval.assess("What is the capital of Japan?")
def test_japan_capital(self):
    return "Tokyo"
```

### Evaluation with Custom Model

```python
@langval.assess(model=custom_llm, question="Who wrote 'Pride and Prejudice'?")
def test_author(self):
    return "Jane Austen"
```

## Contributing

Please read our [CONTRIBUTING.md](CONTRIBUTING.md) file for more detailed information on our contribution process.

## License

Langval is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.