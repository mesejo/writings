a = [1, 2, 3, 4, 2, 6, 1, 1, 5, 2]

res = list(dict.fromkeys(a, None))
print(res)  # [1, 2, 3, 4, 6, 5]

