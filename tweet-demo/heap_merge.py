import heapq

res = heapq.merge([1, 2, 3], [2, 3, 5, 6])
print(list(res))  # [1, 2, 2, 3, 3, 5, 6]
