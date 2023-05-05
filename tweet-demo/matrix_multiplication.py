import numpy as np

test_array = np.array([[0, 0, 1],
                       [1, 1, 0],
                       [1, 1, 1]])

classes = ['a', 'b', 'c']

res = test_array.astype('O') @ classes
print(res)  # ['c' 'ab' 'abc']
