import trrex as tx
import pandas as pd

df = pd.DataFrame(["The quick brown fox",
                   "jumps over",
                   "the lazy dog"],
                  columns=["text"])

trrex = tx.make(["dog", "fox"])
res = df["text"].str.contains(trrex)
print(res)  # [True, False, True]
