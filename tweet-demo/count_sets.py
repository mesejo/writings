from collections import Counter

data = [{1, 2, 3}, {3, 1, 2}, {1, 2}, {3, 4}, {2, 1}]
counts = Counter(map(frozenset, data))  # remember, sets are not hashable
print(counts)  # {frozenset({1, 2, 3}): 2, frozenset({1, 2}): 2, frozenset({3, 4}): 1}
