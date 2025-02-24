# Simple binary tree class, with NON-RECURSIVE operations

# Needed for stack and queue.
from collections import deque


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.value)

    def to_list_depth_first(self):
        stack = deque()
        df_list = []
        stack.append(self)
        print(stack)
        while len(stack)>0:
            node = stack.pop()
            df_list.append(node.value)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            print(stack)
        return df_list

    def to_list_df_inorder(self):
        stack = deque()
        df_list = []
        current = self
        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                df_list.append(current.value)
                current = current.right
            else:
                break
        return df_list

    def to_list_df_postorder(self):
        s1 = deque()
        s2 = deque()
        df_list = []
        s1.append(self)
        while s1:
            node = s1.pop()
            s2.append(node)
            if node.left:
                s1.append(node.left)
            if node.right:
                s1.append(node.right)
        while s2:
            node = s2.pop()
            df_list.append(node.value)
        return df_list


def main() -> None:
    tree = Node(
        1,
        Node(
            2,
            Node(4),
            Node(5)
        ),
        Node(
            3,
            Node(6),
            Node(7)
        )
    )
    print(tree)
    print(tree.to_list_depth_first())
    print(tree.to_list_df_inorder())
    print(tree.to_list_df_postorder())


if __name__ == '__main__':
    main()