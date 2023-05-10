from itertools import zip_longest

fruits = ["apple", "banana", "coconut"]
vegetables = ["spinach", "lettuce"]

res = [item for pack in zip_longest(fruits, vegetables) for item in pack if item]
print(res)