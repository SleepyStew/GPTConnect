function_handler = None


def GPTFunctionHandler(
    group: str = None, description: str = None, params: dict = None
) -> callable:
    """
    Decorator for setting the custom function handler
    """

    def decorator(function):
        global function_handler

        def wrapper(*args, **kwargs):
            return function(*args, **kwargs)

        function_handler = function

        return wrapper

    return decorator
