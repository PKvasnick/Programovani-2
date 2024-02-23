datasets = [
    ["AGGTAB", 'GXTXAYB'],
    ['ABCDGH', 'AEDFHR'],
    ["GAATTCAGTTA","GGATCGA"]
]


def print_matrix(d: list[list[int]]) -> None:
    for row in range(len(d)):
        print(*d[row])
    print()


def lcs(s1:str, s2:str) -> int:
    d = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
    for row in range(1,len(s1)+1):
        c = s1[row-1]
        for col in range(1, len(s2)+1):
            if s2[col-1] != c:
                    d[row][col] = max(d[row][col-1], d[row-1][col])
            else:
                d[row][col] = d[row-1][col-1] + 1
        print_matrix(d)
    return d[-1][-1]


def main() -> None:
    global datasets
    s1, s2 = datasets[2]
    maxlen = lcs(s1, s2)
    print(maxlen)


if __name__ == "__main__":
    main()
