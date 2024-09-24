


class EvalTest:
    registry = {}


    @classmethod
    def register(cls, toxicity: float, accuracy: float, hallucination: float, bias: float):
        def decorator(test_class):
            cls.registry[test_class.__name__] = {
                'class': test_class,
                'metrics': {
                    'toxicity': toxicity,
                    'accuracy': accuracy,
                    'hallucination': hallucination,
                    'bias': bias
                }
            }
            return test_class
        return decorator

    @classmethod
    def eval(cls, input_text: str):
        def decorator(func):
            setattr(func, 'eval_input', input_text)
            return func
        return decorator