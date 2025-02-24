from random import randint


def quick_sort(b):
    if len(b) < 2:
        return b
    if len(b) == 2:
        return [min(b), max(b)]
    pivot = b[randint(0, len(b)-1)]
    lows = [x for x in b if x < pivot]
    pivots = [x for x in b if x == pivot]
    highs = [x for x in b if x > pivot]
    return quick_sort(lows) + pivots + quick_sort(highs)


data = [randint(1,100) for _ in range(10)]

print(data)
print(quick_sort(data))