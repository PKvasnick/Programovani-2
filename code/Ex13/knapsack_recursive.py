from itertools import product


W0 = 10
v = [10, 40, 30, 50]
w = [5, 4, 6, 3]


def solve_knapsack(s, W):
    print(s, W)
    if not s or not W:
        return 0
    new_s = s.copy()
    new_i = new_s.pop(0)
    if w[new_i] > W:
        return solve_knapsack(new_s, W)
    else:
        return max(v[new_i] + solve_knapsack(new_s, W-w[new_i]), solve_knapsack(new_s, W))


def main() -> None:
    all_i = [i for i in range(len(w))]
    print(solve_knapsack(all_i, W0))


if __name__ == "__main__":
    main()