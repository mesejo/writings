from operator import add
from itertools import starmap

first_list, second_list = [1, 2], [2, 3]

res = map(add, first_list, second_list)
print(list(res))  # [3, 5]

res = starmap(add, zip(first_list, second_list))
print(list(res))  # [3, 5]
