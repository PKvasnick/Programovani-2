from random import randint

def insertion_sort(b):
    for i in range(1, len(b)):
        up = b[i]
        j = i - 1
        while j >= 0 and b[j] > up:
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = up
    return b


data = [randint(1,100) for _ in range(10)]

print(data)
print(insertion_sort(data))