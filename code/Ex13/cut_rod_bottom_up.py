def cut_rod_bottom_up(price, n):
    val = [0 for x in range(n + 1)]

    for i in range(1, n + 1):
        max_val = -1
        for j in range(i):
            max_val = max(max_val, price[j] + val[i - j - 1])
        val[i] = max_val

    return val


def main():
    # Example usage
    price = [1, 5, 8, 9, 10, 17, 17, 20]
    n = len(price)
    print("Prices:")
    print("", *range(1, n + 1), sep="\t")
    print("", *price, sep="\t")
    val = cut_rod_bottom_up(price, n)
    print("Subproblems table:")
    print(*range(n + 1), sep="\t")
    print(*val, sep="\t")

    print(f"Maximum obtainable value is {val[-1]}")


if __name__ == "__main__":
    main()
