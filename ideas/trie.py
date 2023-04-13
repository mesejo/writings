import re


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# def regex_trie(node, current_regex):
#     regex = current_regex
#     if node.is_word:
#         regex += "|"
#     for char, child_node in node.children.items():
#         if node.is_word:
#             regex += "("
#         regex += char
#         regex = regex_trie(child_node, regex + ")")
#     return regex

def trie_to_regex(node):
    if not node.children:
        return ""

    if node.is_word:
        if len(node.children) == 1:
            child_char, child_node = next(iter(node.children.items()))
            return node.char + trie_to_regex(child_node)
        else:
            return "(?:" + node.char + trie_to_regex(TrieNode(children=node.children)) + ")?"

    char_groups = []
    for child_char, child_node in node.children.items():
        char_groups.append(
            re.escape(child_char) + trie_to_regex(child_node)
        )

    return "(?:" + "|".join(char_groups) + ")"

# trie.insert("hello")
# trie.insert("world")
# trie.insert("hi")
# trie.insert("hey")
# print(trie.search("hello"))  # True
# print(trie.search("he"))  # False
# print(trie.starts_with("hi"))  # True
