from itertools import product


for i, j in product(range(5), range(5)):
    if i % j == 3:
        print(i,j)
        break
