translation = str.maketrans("ab", "ba", "c")  # {97: 98, 98: 97, 99: None}
res = "ablloonc".translate(translation)
print(res)  # balloon
