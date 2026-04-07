from collections.abc import Hashable, Iterable


def unique[H: Hashable](xs: Iterable[H]) -> set[H]:
    return set(xs)


def main():
    print(unique([1, 1, 2, 3, 3, 4, 5]))


if __name__ == "__main__":
    main()
