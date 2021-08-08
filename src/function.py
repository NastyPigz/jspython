from .exceptions import *

def function(func: set, **kwargs):
    if not kwargs.get("name"):
        run=True
    else:
        run=False
    if run:
        def python_function():
            for i in func:
                i
        return python_function()
    raise NotSupported