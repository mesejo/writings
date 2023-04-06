import shlex

string = 'this is "a test"'

result = shlex.split(string)
print(result)  # ['this', 'is', 'a test']
