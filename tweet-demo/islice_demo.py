from itertools import islice

iterator = islice(range(10), 5, 10, 2)
res = list(iterator)
print(res)  # [5, 7, 9]
