import mmh3
import pandas as pd

n_partitions = 5

s = pd.Series(data=[abs(mmh3.hash(str(key))) % n_partitions for key in range(100_000, 200_000)])
res = s.value_counts(sort=False)
print(res)

# 0    20059
# 3    20134
# 1    20074
# 2    19868
# 4    19865
# Name: count, dtype: int64
