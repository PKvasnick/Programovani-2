def move(n: int, start: str, end: str, via: str) -> None:
    if n == 1:
        print(f"Premistit z {start} na {end}")
    else:
        move(n-1, start, via, end)
        move(1, start, end, via)
        move(n-1, via, end, start)
    return


def main() -> None:
    move(5, "1", "3", "2")


if __name__ == "__main__":
    main()