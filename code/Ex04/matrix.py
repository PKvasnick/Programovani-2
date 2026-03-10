# This module implements a matrix class, with matrix data stored in a flat list.
# We start by implementing basic matrix operations.


class Matrix:
    def __init__(self, rows, cols, value=0):
        self.rows = rows
        self.cols = cols
        self.data = [0] * (rows * cols)

    def __getitem__(self, index):
        row, col = index
        return self.data[row * self.cols + col]

    def __setitem__(self, index, value):
        row, col = index
        self.data[row * self.cols + col] = value

    def __str__(self):
        strmat = []
        for row in range(self.rows):
            strmat.append(
                " ".join(map(str, self.data[row * self.cols : (row + 1) * self.cols]))
            )
        return "\n".join(strmat)

    def __repr__(self):
        return f"Matrix object with dimensions {self.rows}x{self.cols}: " + repr(
            self.data
        )

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows * self.cols):
            result.data[i] = self.data[i] + other.data[i]
        return result

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows * self.cols):
            result.data[i] = self.data[i] + other.data[i]
        return result

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Matrices must have compatible dimensions")
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                result[i, j] = sum(self[i, k] * other[k, j] for k in range(self.cols))
        return result

    def __eq__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            return False
        return all(
            self[i, j] == other[i, j]
            for i in range(self.rows)
            for j in range(self.cols)
        )

    def reshape(self, rows, cols):
        if rows * cols != self.rows * self.cols:
            raise ValueError("Cannot reshape matrix to the given dimensions")
        result = Matrix(rows, cols)
        result.data = self.data.copy()
        return result

    def vec(self):
        return self.reshape(self.rows * self.cols, 1)

    def flatten(self):
        return self.reshape(1, self.rows * self.cols)

    def transpose(self):
        result = Matrix(self.cols, self.rows)
        result.data = [
            self.data[j * self.cols + i]
            for i in range(self.cols)
            for j in range(self.rows)
        ]
        return result


def main():
    m = Matrix(3, 4)
    for i in range(m.rows):
        for j in range(m.cols):
            m[i, j] = i + j
    print(m)
    print(m + m)
    print(m.vec())
    print(m.flatten())
    print(m.transpose())
    print(m * m.transpose())


if __name__ == "__main__":
    main()
