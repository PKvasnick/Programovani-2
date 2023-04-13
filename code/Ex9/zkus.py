# A simple Sudoku solver
import sys

grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]


def print_grid() -> None:
    global grid
    for row in grid:
        print(*row)


def is_admissible(x: int, y: int, digit: int) -> bool:
    global grid
    for col in range(len(grid)):
        if grid[x][col] == digit:
            return False
    for row in range(len(grid)):
        if grid[row][y] == digit:
            return False
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for ix in range(3):
        for iy in range(3):
            if grid[x0 + ix][y0 + iy] == digit:
                return False
    return True


def solve() -> None:
    global grid
    for x in range(len(grid)):
        for y in range(len(grid)):
            if grid[x][y] == 0:
                for digit in range(1, 10):
                    if is_admissible(x, y, digit):
                        grid[x][y] = digit
                        solve()
                        grid[x][y] = 0
                return
    print_grid()
    c = input("Continue?")
    return


print_grid()
print("Solution:")
solve()
