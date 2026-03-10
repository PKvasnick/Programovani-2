from itertools import pairwise
from random import randint

data = [randint(0, 100) for _ in range(20)]

data.sort()
max_spacing = max(q - p for p, q in pairwise(data))
print(*data)
print(max_spacing)
