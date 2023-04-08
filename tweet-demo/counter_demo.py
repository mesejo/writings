from collections import Counter

D1 = Counter({'A': 2, 'B': 1, 'C': 4, 'D': 5})
D2 = Counter({'A': 3, 'B': 4, 'C': 4, 'D': 7})

print(D1 & D2)  # {'D': 5, 'C': 4, 'A': 2, 'B': 1} intersection:  min(D1[x], D2[x])
print(D2 | D1)  # {'D': 7, 'B': 4, 'C': 4, 'A': 3} union: max(D1[x], D2[x])
print(D2 - D1)  # {'B': 3, 'D': 2, 'A': 1} subtract (keeping only positive counts)
print(D2 + D1)  # {'D': 12, 'C': 8, 'A': 5, 'B': 5} add
