from collections import deque


class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    def __len__(self):
        count = 1
        if self.left is not None:
            count += len(self.left)
        if self.right is not None:
            count += len(self.right)
        return count

    def leave_values(self):
        leaves = []
        if self.left is None and self.right is None:
            leaves.append(self.value)
            return leaves
        if self.left is not None:
            leaves.extend(self.left.leave_values())
        if self.right is not None:
            leaves.extend(self.right.leave_values())
        return leaves

    def to_dict(self):
        return {
            "value" : self.value,
            "left" : self.left.to_dict() if self.left else None,
            "right" : self.right.to_dict() if self.right else None
        }

    def __repr__(self):
        return str(self.to_dict())

    def to_list_pre(self):
        nodes = []
        nodes.append(self.value)
        if self.left:
            nodes.extend(self.left.to_list_pre())
        if self.right:
            nodes.extend(self.right.to_list_pre())
        return nodes

    def to_list_in(self):
        nodes = []
        if self.left:
            nodes.extend(self.left.to_list_in())
        nodes.append(self.value)
        if self.right:
            nodes.extend(self.right.to_list_in())
        return nodes

    def to_list_post(self):
        nodes = []
        if self.left:
            nodes.extend(self.left.to_list_post())
        if self.right:
            nodes.extend(self.right.to_list_post())
        nodes.append(self.value)
        return nodes

    def to_string(self, level=0):
        strings = []
        if self.right is not None:
            strings.append(self.right.to_string(level + 1))
        strings.append(' ' * 4 * level + '--> ' + str(self.value))
        if self.left is not None:
            strings.append(self.left.to_string(level + 1))
        return "\n".join(strings)

    def __str__(self):
        return self.to_string()

    def to_list_depth_first(self):
        stack = deque()
        nodes = []
        stack.append(self)
        print(stack)
        while len(stack)>0:
            node = stack.pop()
            nodes.append(node.value)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            print(stack)
        return nodes

    def to_list_breadth_first(self):
        queue = deque()
        nodes = []
        queue.append(self)
        print(queue)
        while len(queue)>0:
            node = queue.popleft()
            nodes.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            print(queue)
        return nodes


def main() -> None:
    tree = Node(
        5,
        Node(6,
             Node(7),
             Node(8)
             ),
        Node(4,
             Node(5),
             Node(2)
             )
    )
    print(tree)
    print(tree.to_list_depth_first())
    print(tree.to_list_breadth_first())


if __name__ == '__main__':
    main()

