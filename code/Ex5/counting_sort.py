from random import randint


def count_sort(b:list[int], rmax: int) -> list[int]:

    bins = [0] * rmax
    for elem in b:
        bins[elem] += 1
    for i in range(rmax):
        if i==0:
            continue
        b[i] += b[i-1]
    b_index = 0
    for ibin, count in enumerate(bins):
        for i in range(count):
            b[b_index] = ibin
            b_index += 1
    return b


r = 10
data = [randint(0,r-1) for _ in range(100)]

print(*data)
print(*count_sort(data, r))