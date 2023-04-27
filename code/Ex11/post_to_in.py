import sys

ops = ["+", "-", "*", "/"]


class Node:
    ...


class Constant(Node):
    def __init__(self, value: int):
        self.value = value

    def __str__(self):
        return str(self.value)


class Operation(Node):
    def __init__(self, op:str, left:Node = None, right:Node = None):
        self.op = op
        self.left = left
        self.right = right

    def needs_brackets_left(self) -> bool:
        left_op = "."
        if isinstance(self.left, Operation):
            left_op = self.left.op
        if self.op in ["*", "/"]:
            if left_op in ["+", "-"]:
                return True
            else:
                return False
        return False

    def needs_brackets_right(self) -> bool:
        right_op = "."
        if isinstance(self.right, Operation):
            right_op = self.right.op
        if self.op == "*":
            if right_op in ["+", "-"]:
                return True
            else:
                return False
        if self.op == "/":
            if right_op in ops:
                return True
            else:
                return False
        if self.op == "-":
            if right_op in ["+", "-"]:
                return True
            else:
                return False
        return False

    def __str__(self):
        left_string = f"{self.left}"
        if self.needs_brackets_left():
            left_string = "(" + left_string + ")"
        right_string = f"{self.right}"
        if self.needs_brackets_right():
            right_string = "(" + right_string + ")"

        return left_string + f"{self.op}" + right_string


def postfix_to_tree() -> Node:
    stack = []
    for term in input().split():
        if term in ops:
            right = stack.pop()
            left = stack.pop()
            stack.append(Operation(term, left, right))
        else:
            stack.append(Constant(int(term)))
    return stack.pop()


def main() -> None:
    tree = postfix_to_tree()
    print(tree)


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    main()
