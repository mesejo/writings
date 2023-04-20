from itertools import groupby


def all_equal(iterable):
    """Returns True if all the elements are equal to each other"""
    g = groupby(iterable)
    return next(g, True) and not next(g, False)


print(all_equal([1, 1, 1]))  # True
print(all_equal([1, 1, 2]))  # False
