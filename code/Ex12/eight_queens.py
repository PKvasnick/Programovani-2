# Place SIZE queens on a chessboard such that
# 1. No pair of queens attack each other
# 2. Each field is under control of a queen

from itertools import product

SIZE = 8


@lambda cls: cls()  # Create class instance immediately
class Chessboard:
    def __init__(self):
        """Just create chessboard"""
        self.chessboard = dict([((i,j),set()) for i, j in product(range(SIZE), range(SIZE))])
        self.queens = []

    def is_in_range(self, k, l):
        return (k,l) in self.chessboard.keys()

    def is_available(self, i, j):
        """Is this field available for a queen?"""
        return len(self.chessboard[i,j]) == 0

    def queen_fields(self, i, j):
        """Return a list of fields controlled by a queen at (i, j)"""
        steps = [(s, t) for s, t in product([-1,0,1], repeat=2) if not s==t==0]
        fields = set()
        for s, t in steps:
            k = i
            l = j
            while self.is_in_range(k, l):
                fields.add((k, l))
                k = k + s
                l = l + t
        return fields

    def place_queen(self, i, j):
        """Place a new queen at i, j"""
        self.queens.append((i,j))
        for k,l in self.queen_fields(i, j):
            self.chessboard[k, l].add((i,j))

    def remove_queen(self):
        """Remove most recently added queen"""
        i, j = self.queens.pop()
        for k, l in self.queen_fields(i, j):
            try:
                self.chessboard[k, l].remove((i,j))
            except KeyError:
                print(f"Error removing ({i=}, {j=} from {self.chessboard[k, l]}")

    def print(self):
        chart = [["_" for _ in range(SIZE)] for _ in range(SIZE)]
        for pos, occ in self.chessboard.items():
            if len(occ) > 0:
                i, j = pos
                chart[i][j] = "o"
        for i, j in self.queens:
            chart[i][j] = "O"
        for i in range(SIZE):
            print(*chart[i])


def place_queens(k = 0):
    global Chessboard
    if k == 8:
        print("\nSolution:")
        Chessboard.print()
        return 8
    for i in range(SIZE):
        if not Chessboard.is_available(k, i):
            continue
        Chessboard.place_queen(k,i)
        place_queens(k+1)
        Chessboard.remove_queen()
    return k


def main():
    place_queens(0)


if __name__ == '__main__':
    main()


