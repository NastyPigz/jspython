import typing
from .new_vals import *

class GlobalVars:
    def __init__(self):
        self.variables = []

    def _add(self, _var: typing.Union[dict]):
        self.variables.append(_var)

global_vars = GlobalVars()

def var(*args, **kwargs: typing.Union[Any]) -> None:
    """
    """
    results={}
    if not args is []:
        for i in args:
            global_vars._add({
                "name": str(i),
                "value": undefined
            })
            results[str(i)]=undefined
    if not kwargs is {}:
        for key, value in kwargs.items():
            global_vars._add(
                {
                    "name": str(key),
                    "value": value
                }
            )
            results[str(key)]=undefined
    if results == {}:
        raise Exception("No variables were provided")
    return results