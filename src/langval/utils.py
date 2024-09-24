import inspect


def check_type(obj):
    """
    Checks if the object is a class or a function
    Args:
        obj (object): The object to check
    Returns:
        str: The type of the object
    """
    if inspect.isclass(obj):
        return "class"
    elif inspect.isfunction(obj):
        return "function"
    else:
        raise TypeError("neither class nor function")
