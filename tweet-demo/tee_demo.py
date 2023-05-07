from itertools import tee

a = [1, 2, 3, 4]
b, c = tee(a)

next(c)
# 1

for i, j in zip(b, c):
    print(i, j)

# (1, 2)
# (2, 3)
# (3, 4)
