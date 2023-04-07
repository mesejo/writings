import re


class Counter:

    def __init__(self, start=0):
        self.counter = start

    def repl(self, match):
        current = self.counter
        self.counter += 1
        return f"{match.group()}-{current}"


counter = Counter()
res = re.sub("apple", counter.repl, "apple, apple, banana, apple")
print(res)  # apple-0, apple-1, banana, apple-2

