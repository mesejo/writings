import pprint

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

rotated = [list(reversed(col)) for col in zip(*matrix)]

pprint.pprint(rotated, width=30)
# [[7, 4, 1],
#  [8, 5, 2],
#  [9, 6, 3]]

