# Simple binary tree class with RECURSIVE methods
from collections import deque

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def to_string(self, level = 0):
        TABS = "    "
        strings = []
        if self.left is not None:
            strings.append(self.left.to_string(level + 1))
        strings.append(TABS * level + '-> ' + str(self.value))
        if self.right is not None:
            strings.append(self.right.to_string(level + 1))
        return "\n".join(strings)

    def __str__(self):
        return self.to_string()

    def to_dict(self):
        repr_dict = {
            "value" : self.value,
            "left" : self.left.to_dict() if self.left is not None else None,
            "right" : self.right.to_dict() if self.right is not None else None
        }
        return repr_dict

    def __repr__(self):
        return str(self.value)

    def to_list_depth_first(self):
        stack = deque()
        values = []
        stack.append(self)
        while stack:
            print(stack)
            node = stack.pop()
            values.append(node.value)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return values

    def to_list_breadth_first(self):
        queue = deque()
        values = []
        queue.append(self)
        while queue:
            print(queue)
            node = queue.popleft()
            values.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return values

    def to_list_preorder_gen(self):
        stack = [self]
        while stack:
            node = stack.pop()
            yield node.value
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return



def main() -> None:
    tree = Node(
        5,
        Node(
            6,
            Node(7),
            Node(8)
        ),
        Node(
            4,
            Node(5),
            Node(2)
        )
    )
    print(tree)
    print(tree.to_list_depth_first())
    print(tree.to_list_breadth_first())
    print(list(tree.to_list_preorder_gen()))


if __name__ == '__main__':
    main()