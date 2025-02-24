from operator import add, sub, mul, floordiv


operators = {
    "+": {"priority": 1, "function": add},
    "-": {"priority": 1, "function": sub},
    "*": {"priority": 2, "function": mul},
    "/": {"priority": 2, "function": floordiv}
}


def is_operator(s: str) -> bool:
    return s in operators


def infix_to_postfix(infix):
    postfix = []
    op_stack = []
    for s in infix:
        if is_operator(s):
            while op_stack and (operators[s]["priority"] <= operators[op_stack[-1]]["priority"]):
                yield op_stack.pop()
            op_stack.append(s)
        else:
            yield s
    while op_stack:
        yield op_stack.pop()
    return


class Node:
    ...


class Constant(Node):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value

    def print(self, level=0):
        TAB = " " * 4
        SEP = " --> "
        print(TAB * level + SEP + str(self.value))

    def get_priority(self):
        return 3


class Operation(Node):
    def __init__(self, opstring):
        self.opstring = opstring
        self.priority = operators[opstring]["priority"]
        self.operation = operators[opstring]["function"]
        self.left = None
        self.right = None

    def eval(self):
        return self.operation(self.left.eval(), self.right.eval())

    def print(self, level=0):
        TAB = " " * 4
        SEP = " --> "
        if self.left:
            self.left.print(level + 1)
        print(TAB * level + SEP + self.opstring)
        if self.right:
            self.right.print(level + 1)

    def get_priority(self):
        return self.priority


def read_infix():
    while True:
        s = input().strip()
        if s == "=":
            break
        yield s
    return


def main() -> None:
    print(*infix_to_postfix(read_infix()))

stack = []
root = None
postfix = infix_to_postfix(read_infix())
for p in postfix:
    if is_operator(p):
        root = Operation(p)
        root.right = stack.pop()
        root.left = stack.pop()
        stack.append(root)
    else:
        stack.append(Constant(int(p)))

root = stack.pop()
root.print()
print(root.eval())


if __name__ == "__main__":
    main()
