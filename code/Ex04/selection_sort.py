from random import randint


def selection_sort(b):
    for i in range(len(b) -1):
        j = b.index(min(b[i:]))
        b[i], b[j] = b[j], b[i]
    return b


data = [randint(1,100) for _ in range(10)]

print(data)
print(selection_sort(data))