from random import sample
# Simple binary tree class, with NON-RECURSIVE operations

# Needed for stack and queue.
from collections import deque


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.cumvalue = 0
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.value)

    def to_string(self, level = 0):
        strings = []
        if self.left is not None:
            strings.append(self.left.to_string(level + 1))
        strings.append(' ' * 4 * level + '-> ' + str(self.cumvalue))
        if self.right is not None:
            strings.append(self.right.to_string(level + 1))
        return "\n".join(strings)

    def set_cumvalues(self) -> None:
        self.cumvalue = self.value
        stack = [self]
        while stack:
            node = stack.pop()
            if node.left:
                node.left.cumvalue = node.cumvalue + node.left.value
                stack.append(node.left)
            if node.right:
                node.right.cumvalue = node.cumvalue + node.right.value
                stack.append(node.right)

    def to_list_depth_first(self):
        stack = deque()
        df_list = []
        stack.append(self)
        print(stack)
        while len(stack)>0:
            node = stack.pop()
            df_list.append(node.value)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            print(stack)
        return df_list

    def to_list_breadth_first(self):
        queue = deque()
        bf_list = []
        queue.append(self)
        print(queue)
        while len(queue)>0:
            node = queue.popleft()
            bf_list.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            print(queue)
        return bf_list


def tree_from_list(values: list[int]) -> Node:
    values = [0] + values
    queue = deque()
    index = 1
    tree = Node(values[index])
    print(index)
    index += 1
    queue.append(tree)
    while index < len(values):
        node = queue.popleft()
        node.left = Node(values[index])
        index += 1
        queue.append(node.left)
        if index == len(values):
            node.right = None
            break
        node.right = Node(values[index])
        index += 1
        queue.append(node.right)
    return tree


def main() -> None:
    source = list(range(-16, 17))
    values = sample(source, len(source))
    tree = tree_from_list(values)
    tree.set_cumvalues()
    print(tree.to_string())


if __name__ == '__main__':
    main()