class BaseLangvalError(Exception):
    """
    Base class for all langval errors.
    """

    pass


class EvalThreshold(BaseLangvalError):
    def __init__(self, breached_value: dict):
        self.breached_value = breached_value

    def __str__(self):
        return f"Validation failed. {self.breached_value}"
