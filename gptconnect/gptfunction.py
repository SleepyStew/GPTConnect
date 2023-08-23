from typing import Dict, Union

from gptconnect import functions
from .dataclasses import Params


def GPTFunction(
    group: str = "default", description: str = "", params: Union[Params, Dict] = None
) -> callable:
    """
    Decorator for creating a GPT function

    :param group: The group of the function
    :param description: The description of the function
    :param params: The parameters of the function, as a Params object or as a dictionary
    """

    def decorator(function):
        def wrapper(*args, **kwargs):
            return function(*args, **kwargs)

        if isinstance(params, Params):
            params_ = {
                "type": "object",
                "properties": params.properties_dict(),
                "required": params.required,
            }
        elif isinstance(params, dict):
            params_ = params
        elif params is None:
            params_ = {
                "type": "object",
                "properties": {},
                "required": [],
            }
        else:
            raise TypeError(
                f"params must be a Params object or a dictionary, not {type(params)}"
            )

        details = {
            "function": function,
            "group": group,
            "name": function.__name__,
            "description": description,
            "parameters": params_,
        }

        functions.append(details)

        return wrapper

    return decorator
