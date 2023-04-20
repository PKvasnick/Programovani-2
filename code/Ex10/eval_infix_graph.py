from operator import add, sub, mul, floordiv

operators = {
    "+": {"priority":1, "function":add},
    "-": {"priority":1, "function": sub},
    "*": {"priority":2, "function": mul},
    "/": {"priority":2, "function": floordiv}
}

class Node:
    ...


class Constant(Node):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value

    def print(self, level = 0):
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

    def print(self, level = 0):
        TAB = " " * 4
        SEP = " --> "
        if self.left:
            self.left.print(level + 1)
        print(TAB * level + SEP + self.opstring)
        if self.right:
            self.right.print(level + 1)

    def get_priority(self):
        return self.priority


roots = [None]
while True:
    root = roots.pop()
    opstr = input().strip()
    if opstr == "=":
        roots.append(root)
        root = roots[0]
        break
    if opstr in operators:
        new_root = Operation(opstr)
        root_priority = root.get_priority()
        new_priority = new_root.get_priority()
        if new_priority > root_priority:
            roots.append(root)
            right_node = root.right
            root.right = new_root
            new_root.left = right_node
        elif new_priority == root_priority or len(roots) == 0:
            if len(roots) > 0:
                parent = roots.pop()
                if parent.left is root:
                    parent.left = new_root
                elif parent.right is root:
                    parent.right = new_root
                roots.append(parent)
            new_root.left = root
        elif new_priority < root_priority:
            if len(roots) > 0:
                root = roots.pop()
            new_root.left = root
        roots.append(new_root)
    else:
        if not root:
            root = Constant(int(opstr))
        else:
            root.right = Constant(int(opstr))
        roots.append(root)

root.print()
print(root.eval())



