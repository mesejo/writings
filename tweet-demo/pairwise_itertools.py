from itertools import tee


def pairwise(iterable):
    """s -> (s0,s1), (s1,s2), (s2, s3), ..."""
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


words = ['car', 'cat', 'cactus', 'cactii']
for prev_, next_ in pairwise(words):
    print(f"{prev_} => {next_}")

# car => cat
# cat => cactus
# cactus => cactii
