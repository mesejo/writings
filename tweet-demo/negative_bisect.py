import bisect

x = [4.0, 3.0, 2.0, 1.0]
bisect.insort(x, 2.5, key=lambda e: e * -1)
print(x)  # [4.0, 3.0, 2.5, 2.0, 1.0]
