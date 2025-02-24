sequence = []
max_sequence = []
box = [[0 for _ in range(7)] for _ in range(7)]


def print_box() -> None:
    for row in box:
        print(*row, sep = " ")
    print()


def parse_dominoes() -> tuple[int, int]:
    global box
    n, start = [int(s) for s in input().split()]
    dominoes = input().split()
    assert len(dominoes) == n, "Inconsistent parsing of dominoes"
    for d in dominoes:
        assert len(d) == 2, "Incorrect domino " + d
        i, j = [int(c) for c in d]
        box[i][j] += 1
        if i != j:
            box[j][i] += 1
    return n, start


def solve(start: int) -> None:
    global box, sequence, max_sequence
    for i in range(7):
        if box[start][i] > 0:
            box[start][i] -= 1
            if start != i:
                box[i][start] -= 1
            sequence.append(str(start) + str(i))
            if len(sequence) > len(max_sequence):
                max_sequence = sequence.copy()
            solve(i)
            sequence.pop()
            box[start][i] += 1
            if start != i:
                box[i][start] += 1
    return


def main() -> None:
    n, start = parse_dominoes()
    solve(start)
    print(len(max_sequence))
    print(*max_sequence)


if __name__ == "__main__":
    main()