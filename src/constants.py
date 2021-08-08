import typing
from .vars import *
from .new_vals import *
from .exceptions import *

class ConstVars(GlobalVars):
    def __init__(self):
        super().__init__()

    def _add(self, _var: typing.Union[dict]) -> None:
        self.variables.append(_var)
    
    def _isin(self, name: typing.Union[str]) -> typing.Union[bool]:
        result: bool = False
        for vs in self.variables:
            if vs["name"]==str(name):
                result = True
                break
        return result

const_vars = ConstVars()

def const(*args, **kwargs: typing.Union[Any]) -> typing.Union[list]:
    """
    """
    results = {}
    if not args is []:
        for i in args:
            if const_vars._isin(i):
                raise Forbidden("trying to re-declare a const var")
            const_vars._add({
                "name": str(i),
                "value": undefined
            })
            results[str(i)]=undefined
    if not kwargs is {}:
        for key, value in kwargs.items():
            if const_vars._isin(key):
                raise Forbidden("trying to re-declare a const var")
            const_vars._add(
                {
                    "name": str(key),
                    "value": value
                }
            )
            results[str(key)]=value
    if results == {}:
        raise Exception("No constants were provided")
    return results

def w(name:typing.Union[str], value:typing.Union[Any]):
    for v_set in global_vars.variables:
        if v_set["name"] == name:
            v_set["value"]=value


def g(name:typing.Union[str]):
    t=undefined
    for v_set in global_vars.variables:
        if v_set["name"] == name:
            t=v_set
            break
    return t