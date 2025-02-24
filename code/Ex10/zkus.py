class Node:
    ...


class Constant(Node):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"{self.value}"

    def eval(self):
        return self.value

    def derivative(self, by):
        return Constant(0)

    def prune(self):
        return self


class Variable(Node):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def eval(self, env):
        return f"{env[self.name]}"

    def derivative(self, by):
        if self.name == by:
            return Constant(1)
        else:
            return Constant(0)

    def prune(self):
        return self

def is_zero_constant(node):
    return isinstance(node, Constant) and node.value == 0

def is_unit_constant(node):
    return isinstance(node, Constant) and node.value == 1



class Plus(Node):
    def __init__(self, left = None, right = None):
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.left} + {self.right}"

    def eval(self, env):
        return self.left.eval(env) + self.right.eval(env)

    def derivative(self, by):
        return Plus(
            self.left.derivative(by),
            self.right.derivative(by)
        )

    def prune(self):
        if self.left: self.left = self.left.prune()
        if self.right: self.right = self.right.prune()
        if self.left and is_zero_constant(self.left):
            if self.right and is_zero_constant(self.right):
                return Constant(0)
            else:
                return self.right
        if self.right and is_zero_constant(self.right):
            return self.left


class Times(Node):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.left} * {self.right}"

    def eval(self, env):
        return self.left.eval(env) * self.right.eval(env)

    def derivative(self, by):
        return Plus(
            Times(
                self.left.derivative(by),
                self.right
            ),
            Times(
                self.left,
                self.right.derivative(by)
            )
        )

    def prune(self):
        self.left = self.left.prune()
        self.right = self.right.prune()
        if is_zero_constant(self.left) | is_zero_constant(self.right):
            return Constant(0)
        if is_unit_constant(self.left):
            if is_unit_constant(self.right):
                return Constant(1)
            else:
                return self.right
        if is_unit_constant(self.right):
            return self.left
        return self


def main() -> None:
    tree = Plus(
        Variable("x"),
        Times(
            Constant(5),
            Variable("y")
        )
    )

    print(tree)
    # print(tree.eval(env={"x":2, "y":1}))
    print(tree.derivative(by = "x"))
    print(tree.derivative(by = "x").prune())
    print(tree.derivative(by = "y"))
    print(tree.derivative(by = "y").prune())


if __name__ == "__main__":
    main()