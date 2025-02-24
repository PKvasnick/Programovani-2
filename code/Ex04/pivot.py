from random import randint

data = [randint(1,10) for _ in range(10)]


def partial_sort(a: list[int], start: int = None, end: int = None) -> tuple[list[int], int, int]:
    if start is None:
        start = 0
    if end is None:
        end = len(a)
    pivot = a[start]
    l_pivots = start
    r_pivots = start + 1
    p = r_pivots
    while p < end:
        if a[p] < pivot:
            hold = a[p]
            for i in range(p, l_pivots, -1):
                a[i] = a[i-1]
            a[l_pivots] = hold
            l_pivots += 1
            r_pivots += 1
        elif a[p] == pivot:
            hold = a[p]
            for i in range(p, r_pivots, -1):
                a[i] = a[i-1]
            a[r_pivots] = hold
            r_pivots += 1
        p += 1
    return a, l_pivots, r_pivots


print(data)
print(partial_sort(data))



