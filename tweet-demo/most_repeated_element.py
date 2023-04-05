from collections import Counter
from operator import itemgetter

letters = ["a", "a", "b", "c", "d", "b", "a", "d"]
max_counts = Counter(letters).most_common(1)[0]  # DON'T DO THIS
print(max_counts)

max_counts = max(Counter(letters).items(), key=itemgetter(1))
print(max_counts)
