import re

s = "a b c d b"


def repl(e, lookup={"a": "bye", "b": "hay"}):
    return lookup.get(e.group(), e.group)


result = re.sub("[ab]", repl, s)
print(result)  # bye hay c d hay
