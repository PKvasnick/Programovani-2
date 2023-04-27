import sys

ops = ["+", "-", "*", "/"]


class Node:
    ...


class Constant(Node):
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None
        self.left_brackets = 0
        self.right_brackets = 0

    def __str__(self):
        return "(" * self.left_brackets + str(self.value) + ")" * self.right_brackets


class Operation(Node):
    def __init__(self, op:str, left: Node = None, right: Node = None):
        self.op = op
        self.left = left
        self.right = right
        self.left_brackets = 0
        self.right_brackets = 0

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
        return self.op


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


def set_brackets(tree) -> Node:
    stack = [tree]
    while stack:
        node = stack.pop()
        if node.left:
            if node.needs_brackets_left():
                node.left.left_brackets = node.left_brackets + 1
                node.left.right_brackets = 1
            else:
                node.left.left_brackets = node.left_brackets
            stack.append(node.left)
        if node.right:
            if node.needs_brackets_right():
                node.right.left_brackets = 1
                node.right.right_brackets = node.right_brackets + 1
            else:
                node.right.right_brackets = node.right_brackets
            stack.append(node.right)
    return tree


def tree_to_infix(tree: Node):
    stack = []
    current = tree
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            yield str(current)
            current = current.right
        else:
            break


def main() -> None:
    tree = postfix_to_tree()
    tree = set_brackets(tree)
    print("".join(tree_to_infix(tree)))


if __name__ == "__main__":
    main()
