import heapq


def heap_sort(seq):

    shallow = seq[:]
    heapq.heapify(shallow)
    return [heapq.heappop(shallow) for _ in range(len(shallow))]


lst = [3, 4, 2, 1, 6, 5, 7, 8, 9, 0]
print(heap_sort(lst))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


