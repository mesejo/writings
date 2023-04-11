import sre_constants
from sre_constants import IN, BRANCH, RANGE, LITERAL, MAX_REPEAT
from sre_parse import parse, SubPattern

pat = parse("(ab){1,3}")
print(pat, type(pat))


def generate_key_in(t):
    op, av = t
    if op == RANGE:
        return av[0]
    elif op == LITERAL:
        return av


def generate_key(pattern):
    for op, av in pattern.data:
        if op == sre_constants.LITERAL:
            return "".join(map(lambda x: chr(x[1]), pattern.data))
        if op is IN:
            return chr(min(map(generate_key_in, av)))
        elif op is BRANCH:
            return min(generate_key(a) for a in av[1])
        elif op is MAX_REPEAT:
            start, end, pat = av
            if isinstance(pat, SubPattern):
                return generate_key(pat)
            else:
                print(pat)


k = generate_key(pat)
print(k)
