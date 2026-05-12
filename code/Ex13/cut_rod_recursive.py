def cut_rod_naive(price, n):
    if n <= 0:
        return 0
    max_val = float("-inf")
    for i in range(n):
        max_val = max(max_val, price[i] + cut_rod_naive(price, n - i - 1))
    return max_val


def main():
    price = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    n = len(price)
    print(f"Maximum obtainable value is {cut_rod_naive(price, n)}")


if __name__ == "__main__":
    main()
