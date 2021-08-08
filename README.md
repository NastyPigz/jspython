Disclaimer:
This is still in VERY EARLY VERSION OF DEVELOPMENT.

Example of usage:

```py
from src import *

test = const("re", client=require("discord.json"))
test_var = var("global_", global_='ayeyee')
test_error = const(re=require("discord"))
test_new_var = var(global_=undefined)

print(test)
print(test_error)
print(test_var)

function({
    console.log("hi"),
})
```