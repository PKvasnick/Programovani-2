# A simple Sudoku solver

grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
grid2 = [[0, 4, 1, 0, 0, 0, 2, 7, 1],
         [5, 6, 0, 0, 2, 0, 0, 9, 1],
         [3, 0, 8, 0, 0, 0, 5, 0, 6],
         [0, 0, 0, 5, 0, 9, 0, 0, 0],
         [0, 9, 0, 0, 8, 0, 0, 6, 0],
         [0, 0, 0, 6, 0, 7, 0, 0, 0],
         [7, 0, 6, 0, 0, 0, 4, 0, 2],
         [1, 5, 0, 0, 6, 0, 0, 3, 9],
         [0, 3, 9, 0, 0, 0, 6, 1, 0]
         ]

# grid = grid2


def print_grid():
    global grid
    for row in range(9):
        print(*grid[row])
    return


def possible(x, y, n):
    """Is digit n admissible at position x, y in the grid?"""
    global grid
    # row
    for col in range(9):
        if grid[x][col] == n:
            return False
    # column
    for row in range(9):
        if grid[row][y] == n:
            return False
    # block
    row0 = (x // 3) * 3
    col0 = (y // 3) * 3
    for row in range(3):
        for col in range(3):
            if grid[row0+row][col0+col] == n:
                return False
    return True


def analyze_grid() -> None:
    global grid
    for x in range(9):
        for y in range(9):
            if grid[x][y] == 0:
                possibles = []
                for digit in range(1, 10):
                    if possible(x, y, digit):
                        possibles.append(digit)
                print(f"{x=} {y=}:", *possibles)
    return


def solve():
    global grid
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for n in range(1, 10):
                    if possible(row, col, n):
                        grid[row][col] = n
                        solve()
                        grid[row][col] = 0
                return
    print_grid()
    s = input("Continue?")


solve()
