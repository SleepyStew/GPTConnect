from gptconnect import functions


def GPTFunction(
    group: str = None, description: str = None, params: dict = None
) -> callable:
    """
    Decorator for creating a GPT function

    :param group: The group of the function
    :param description: The description of the function
    :param params: The parameters of the function, in OpenAI's standard JSON format
    """

    def decorator(function):
        def wrapper(*args, **kwargs):
            return function(*args, **kwargs)

        details = {
            "function": function,
            "group": group,
            "name": function.__name__,
            "description": description,
            "parameters": params,
        }
        functions.append(details)

        return wrapper

    return decorator
