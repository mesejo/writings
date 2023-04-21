from itertools import groupby

# Find runs of consecutive numbers using groupby.  The key to the solution
# is differencing with a range so that consecutive numbers all appear in
# same group.
data = [1, 4, 5, 6, 10, 15, 16, 17, 18, 22, 25, 26, 27, 28]
for k, g in groupby(enumerate(data), lambda t: t[0] - t[1]):
    print([gi for _, gi in g])
