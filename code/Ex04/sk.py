from random import randint


def argmin(arr: list):
    return arr.index(min(arr))


def selection_sort(arr:list) -> list:
    for i in range(len(arr) -1):
        p = i + argmin(arr[i:])
        arr[i], arr[p] = arr[p], arr[i]
    return arr


data = [randint(1, 100) for i in range(20)]
print(data)
print(selection_sort(data))
