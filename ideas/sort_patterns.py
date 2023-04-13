import re
from io import StringIO
from sre_constants import LITERAL, IN, NEGATE, BRANCH, CATEGORY, CATEGORY_DIGIT, RANGE, MAX_REPEAT, SUBPATTERN, \
    MAXREPEAT
from sre_parse import parse, _parse, Tokenizer, State, IN, SubPattern
from ideas.trie import Trie, TrieNode


def sub_parse(source, state, verbose, nested):
    items = []
    itemsappend = items.append
    sourcematch = source.match
    start = source.tell()
    while True:
        itemsappend(_parse(source, state, verbose, nested + 1,
                           not nested and not items))
        if not sourcematch("|"):
            break

    return items


def extract_max_repeat_node(val):
    start, end, pat = val
    p = ""
    for op, v in pat:
        if op == LITERAL:
            p += extract_literal_node(v)
        elif op == IN:
            p += extract_in_node(v)

    if end == MAXREPEAT:
        return f"{p}+"

    return rf"{p}{{{start},{end}}}"


def to_list(string):
    source = Tokenizer(string)
    state = State()
    state.str = string
    items = sub_parse(source, state, 0, 0)

    return items_to_list(items)


def shallow_items_to_list(item):
    lst = []
    for op, val in item:
        if op == IN:
            lst.append(extract_in_node(val))
        elif op == LITERAL:
            lst.append(extract_literal_node(val))
        elif op == MAX_REPEAT:
            lst.append(extract_max_repeat_node(val))
    return lst


def items_to_list(items):
    res = []
    for item in items:
        lst = []
        for op, val in item:
            if op == IN:
                lst.append(extract_in_node(val))
            elif op == LITERAL:
                lst.append(extract_literal_node(val))
            elif op == MAX_REPEAT:
                lst.append(extract_max_repeat_node(val))
            elif op == SUBPATTERN:
                lst[:] = shallow_items_to_list(val[-1])
        res.append(lst)
    return res


def extract_literal_node(val):
    return chr(val)


def extract_in_node(val):
    ii = ""
    category = False
    for a, v in val:
        if a == CATEGORY:
            if v == CATEGORY_DIGIT:
                ii += r"\d"
            category = True
        elif a == RANGE:
            start, end = v
            ii += f"{chr(start)}-{chr(end)}"
        elif a == LITERAL:
            ii += chr(v)
    return ii if category and len(val) == 1 else f"[{ii}]"


assert [["a", "b+", "c"]] == to_list(r"ab+c")
assert [["a", "b", r"\d"], ["b"]] == to_list(r"(ab\d)|b")
assert [["a", "b", r"[c-z]"], ["b"]] == to_list(r"(ab[c-z])|b")
assert [["a", "b", r"[c-z]", "a{1,3}"], ["b"]] == to_list(r"(ab[c-z]a{1,3})|b")
assert [["a", "b"], ["b"]] == to_list("(ab)|b")
assert [["a"], ["b"]] == to_list("a|b")
assert [["a{1,3}", "[b-z]", r"\d"]] == to_list(r"a{1,3}[b-z]\d")
assert [["a{1,3}", "b", "c", "d"]] == to_list("a{1,3}bcd")
assert [[r"\d{1,3}"]] == to_list(r"\d{1,3}")
assert [["a"]] == to_list("a")
assert [["a", "B"]] == to_list("aB")
assert [[r"[\dabc]"]] == to_list(r"[\dabc]")
assert [[r"\d"]] == to_list(r"\d")
assert [["[a-e]"]] == to_list("[a-e]")
assert [["[a-e]", "x", "y", "z"]] == to_list("[a-e]xyz")
assert [["[a-exyz]"]] == to_list("[a-exyz]")
assert [[r"[a-e\d]"]] == to_list(r"[a-e\d]")
assert [["a{1,3}"]] == to_list("a{1,3}")

patterns = ['ab+',
            'ab+e',
            'ac\d+',
            'a\d+']

trie = Trie()
for p in patterns:
    for e in to_list(p):
        trie.insert(e)

_OPTION = ("?", TrieNode())
_OPEN_PARENTHESIS = ("(?:", TrieNode())
_CLOSE_PARENTHESIS = (")", TrieNode())
_OPEN_BRACKETS = ("[", TrieNode())
_CLOSE_BRACKETS = ("]", TrieNode())
_ALTERNATION = ("|", TrieNode())


def _to_regex(t):
    stack = [("", t.root)]
    cumulative = StringIO()

    while stack:
        char, node = stack.pop()
        cumulative.write(char)

        if not node.children:
            continue  # skip

        if node.is_word:
            stack.append(_OPTION)

        multiple = []
        for key, child in node.children.items():
            multiple.append((key, child))

        requires_alternation = len(multiple) > 1
        requires_group = requires_alternation or node.is_word

        if requires_group:
            stack.append(_CLOSE_PARENTHESIS)

        if multiple:
            head, *tail = multiple
            stack.append(head)

            for child in tail:
                stack.append(_ALTERNATION)
                stack.append(child)

        if requires_group:
            stack.append(_OPEN_PARENTHESIS)

    return cumulative.getvalue()

pat = _to_regex(trie)
pat = re.compile(pat)
print(pat)
for s in ["a123", "ac1234", "ab", "abe", "abbbe", "abbb"]:
    m = pat.match(s)
    print(m)

