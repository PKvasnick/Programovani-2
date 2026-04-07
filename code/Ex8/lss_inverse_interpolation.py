# Build inverse interpolation table using a headless simply linked list

from matplotlib import pyplot as plt


class Node:
    def __init__(self, x):
        self.x: float = x
        self.next = None


class InverseInterpolationTable:
    def __init__(self, func, low, high):
        self.head = None
        self.low: float = low
        self.high: float = high
        self.func = func

    def __str__(self):
        result = []
        this = self.head
        while this:
            result.append(f"{this.x:.2f} : {self.func(this.x):.2f}")
            this = this.next
        return " -> ".join(result)

    def insert_next(self, this, x):
        new_node = Node(x)
        new_node.next = this.next
        this.next = new_node

    def build_table(self, eps=1e-2):
        self.head = Node(self.low)
        self.insert_next(self.head, self.high)
        this = self.head
        while this.next:
            x1 = this.x
            x2 = this.next.x
            xm = 0.5 * (x1 + x2)
            diff = abs(self.func(x2) - self.func(x1))
            diff_1 = abs(self.func(xm) - self.func(x1))
            diff_2 = abs(self.func(x2) - self.func(xm))
            diffmax = max(diff, diff_1, diff_2)
            if diffmax < eps:
                this = this.next
            else:
                self.insert_next(this, xm)

    def get_values(self):
        x = []
        y = []
        this = self.head
        while this:
            x.append(this.x)
            y.append(self.func(this.x))
            this = this.next
        return x, y


def make_function(s: str):
    import math

    def f(x):
        return eval(s, {"x": x, "math": math})

    return f


def main():
    s = input().strip()
    function = make_function(s)
    low = float(input())
    high = float(input())
    table = InverseInterpolationTable(function, low, high)
    table.build_table(0.2)
    print(table)
    x, y = table.get_values()
    plt.scatter(x, y)
    plt.show()


if __name__ == "__main__":
    main()
