# Find the shortest path of the rook on chessboard

import heapq


SIZE = 8
INF = 10_000


@lambda cls: cls()  # Create class instance immediately
class Chessboard:
    def __init__(self):
        """Just create chessboard"""
        self.chessboard = dict([((i,j),INF) for i, j in product(range(SIZE), range(SIZE))])

    def is_in_range(self, k, l):
        return (k,l) in self.chessboard.keys()

    def set_obstacle(self, i, j):
        self.chessboard[i,j] = -1

    def rook_fields(self, i, j):
        """Return a list of fields controlled by a queen at (i, j)"""
        steps = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        fields = []
        for s, t in steps:
            k = i
            l = j
            while self.is_in_range(k, l) and self.chessboard[i,j] != -1:
                fields.add((k, l))
                k = k + s
                l = l + t
        return fields

    def print(self):
        chart = [["_" for _ in range(SIZE)] for _ in range(SIZE)]
        for pos, steps in self.chessboard.items():
            i, j = pos
            if steps == -1:
                chart[i][j] = "x"
        for i, j in self.queens:
            chart[i][j] = "O"
        for i in range(SIZE):
            print(*chart[i])


def main():


if __name__ == '__main__':
    main()


