from itertools import product


W0 = 10
v0 = [10, 40, 30, 50]
w0 = [2, 3, 4, 5]


def print_matrix(d, colnames, rownames):
    for s in ["", *colnames]:
        print(f"{s:5}", end = "")
    print()
    for rowname, row in zip(rownames, d):
        for s in [rowname, *row]:
            print(f"{s:5}", end = "")
        print()
    print()


def knapsack_dp(w, v, W):
    cum_w = list(range(W+1))
    dp = [[0 for _ in range(len(cum_w))] for _ in range(len(w) + 1)]
    for row in range(1, len(dp)):
        w_row = w[row-1]
        v_row = v[row-1]
        print(w_row, v_row)
        for col in range(1, len(cum_w)):
            W_col = cum_w[col]
            if w_row > W_col:
                dp[row][col] = dp[row-1][col]
            else:
                prev_col = cum_w.index(W_col - w_row)
                dp[row][col] = max(dp[row-1][col], v_row + dp[row-1][prev_col])
        print_matrix(dp, cum_w, [0, *w])
    return


def main() -> None:
    knapsack_dp(w0, v0, W0)


if __name__ == "__main__":
    main()