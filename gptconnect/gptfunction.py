from gptconnect import functions


def GPTFunction(description: str = None, params: dict = None, group: str = None):
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
