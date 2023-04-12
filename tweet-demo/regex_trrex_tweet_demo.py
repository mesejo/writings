import regex
import trrex as tx

pattern = tx.make(["monkey", "monster", "dog", "cat"], prefix="", suffix=r"{1<=e<=2}")

res = regex.search(pattern, "This is really a master dag", regex.BESTMATCH)
print(res)  # <regex.Match object; span=(24, 27), match='dag', fuzzy_counts=(1, 0, 0)>
