# Simple binary tree class with RECURSIVE methods


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
        return str(self.to_dict())

    def to_list_preorder(self):
        flat_list = []
        flat_list.append(self.value)
        if self.left is not None:
            flat_list.extend(self.left.to_list_preorder())
        if self.right is not None:
            flat_list.extend(self.right.to_list_preorder())
        return flat_list

    def to_list_inorder(self):
        flat_list = []
        if self.left is not None:
            flat_list.extend(self.left.to_list_inorder())
        flat_list.append(self.value)
        if self.right is not None:
            flat_list.extend(self.right.to_list_inorder())
        return flat_list

    def to_list_postorder(self):
        flat_list = []
        if self.left is not None:
            flat_list.extend(self.left.to_list_postorder())
        if self.right is not None:
            flat_list.extend(self.right.to_list_postorder())
        flat_list.append(self.value)
        return flat_list

    def count(self):
        count = 1
        if self.left is not None:
            count += self.left.count()
        if self.right is not None:
            count += self.right.count()
        return count

    def write_leaves(self):
        if self.left is None and self.right is None:
            return [self.value]
        leaves = []
        if self.left is not None:
            leaves.extend(self.left.write_leaves())
        if self.right is not None:
            leaves.extend(self.right.write_leaves())
        return leaves

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
    print(tree.to_list_preorder())
    print(tree.to_list_inorder())
    print(tree.to_list_postorder())
    print(tree.count())
    print(tree.__repr__())
    print(tree.write_leaves())


if __name__ == '__main__':
    main()