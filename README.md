# langval

langval is a language model evaluation tool for evaluating the toxicity, accuracy, hallucination, and bias of language models.

## Installation

```bash
pip install langval
```

## Usage

```python
from langval.eval import EvalTest
from langval.model import ModuleModel

@EvalTest.register(toxicity=0.5, accuracy=0.8, hallucination=0.2, bias=0.1)
class TestBaseCase(EvalTest):
    def test(self):
        return ModuleModel(name="my_module", type="function", metrics=self.metrics)

langval = Langval()
langval.add_test(MyTest)
langval.run()
```

## Contributing

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) for more information.

## License

langval is licensed under the [MIT License](LICENSE).   
