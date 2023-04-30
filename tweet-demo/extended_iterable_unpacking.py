numbers = list(range(4, 10))

first, *_, last = numbers
print(first, last)  # 4 9

first, second, *_ = numbers
print(first, second)  # 4 5

*_, penultimate, last = numbers
print(penultimate, last) # 8 9
