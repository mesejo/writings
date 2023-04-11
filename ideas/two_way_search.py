

def lex_search(needle: str, len_needle: int, invert_alphabet: bool):
    # Do a lexicographic search. Essentially this:
    # >>> max(needle[i:] for i in range(len(needle)+1))
    # Also find the period of the right half.
    max_suffix = 0
    candidate = 1
    k = 0
    # The period of the right half.
    period = 1

    while candidate + k < len_needle:
        # each loop increases candidate + k + max_suffix
        a = needle[candidate + k]
        b = needle[max_suffix + k]
        # check if the suffix at candidate is better than max_suffix
        if invert_alphabet and b < a or not invert_alphabet and a < b:
            # Fell short of max_suffix.
            # The next k + 1 characters are non-increasing
            # from candidate, so they won't start a maximal suffix.
            candidate += k + 1
            k = 0
            # We've ruled out any period smaller than what's
            # been scanned since max_suffix.
            period = candidate - max_suffix
        elif a == b:
            if k + 1 != period:
                # Keep scanning the equal strings
                k += 1
            else:
                # Matched a whole period.
                # Start matching the next period.
                candidate += period
                k = 0
        else:
            # Did better than max_suffix, so replace it.
            max_suffix = candidate
            candidate += 1
            k = 0
            period = 1

    return max_suffix, period


def factorize(needle):
    """
    Do a "critical factorization", making it so that:
    >>> needle = (left := needle[:cut]) + (right := needle[cut:])
    where the "local period" of the cut is maximal.
    The local period of the cut is the minimal length of a string w
    such that (left endswith w or w endswith left)
    and (right startswith w or w startswith left).
    The Critical Factorization Theorem says that this maximal local
    period is the global period of the string.
    Crochemore and Perrin (1991) show that this cut can be computed
    as the latter of two cuts: one that gives a lexicographically
    maximal right half, and one that gives the same with the
    with respect to a reversed alphabet-ordering.
    This is what we want to happen:
    >>> x = "GCAGAGAG"
    >>> cut, period = factorize(x)
    >>> x[:cut], (right := x[cut:])
    ('GC', 'AGAGAG')
    >>> period  # right half period
    2
    >>> right[period:] == right[:-period]
    True
    This is how the local period lines up in the above example:
             GC | AGAGAG
    AGAGAGC = AGAGAGC
    The length of this minimal repetition is 7, which is indeed the
    period of the original string.
    """
    len_needle = len(needle)
    cut1, period1 = lex_search(needle, len_needle, invert_alphabet=False)
    cut2, period2 = lex_search(needle, len_needle, invert_alphabet=True)

    # Take the later cut.
    if cut1 > cut2:
        period = period1
        cut = cut1
    else:
        period = period2
        cut = cut2

    print("split: ", needle[:cut], " + ", needle[cut:])
    return cut, period

print(factorize("GCAGAGAG"))
print(factorize("abcdEFGH"))
print(factorize("cdEFGH"))
print(factorize("AAbAAbAAbA"))