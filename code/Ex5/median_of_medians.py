from random import randint


def insertion_sort(b: list[int]) -> list[int]:
    for i in range(1, len(b)):
        key = b[i]
        j = i - 1
        while j >= 0 and b[j] > key:
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = key
    return b


def median(b: list[int]) -> int:
    b = insertion_sort(b)
    mid = len(b) // 2
    return (b[mid] + b[~mid]) // 2


def median_of_medians(b: list[int]) -> int:
    if len(b) <= 5:
        return median(b)
    medians = [median(b[i : i + 5]) for i in range(0, len(b), 5)]
    return median_of_medians(medians)


def main():
    b = [randint(1, 100) for _ in range(100)]
    print(median_of_medians(b))
    print(median(b))


if __name__ == "__main__":
    main()
