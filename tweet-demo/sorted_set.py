from collections.abc import MutableSet

class SortedSet(MutableSet):

    def __init__(self, iterable):
        self.elements = set(iterable)

    def __iter__(self):
        return iter(sorted(self.elements))

    def __contains__(self, value):
        return value in self.elements

    def __len__(self):
        return len(self.elements)

    def add(self, value):
        self.elements.add(value)

    def discard(self, value):
        self.elements.discard(value)

ss = SortedSet([1, 2, 2, 3, 4])
print(list(ss))
