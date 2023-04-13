class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    def count(self):
        count = 1
        if self.left:
            count += self.left.count()
        if self.right:
            count += self.right.count()
        return count

    def to_list_preorder(self):
        node_list = []
        node_list.append(self.value)
        if self.left:
            node_list.extend(self.left.to_list_preorder())
        if self.right:
            node_list.extend(self.right.to_list_preorder())
        return node_list

    def to_list_inorder(self):
        node_list = []
        if self.left:
            node_list.extend(self.left.to_list_inorder())
        node_list.append(self.value)
        if self.right:
            node_list.extend(self.right.to_list_inorder())
        return node_list

    def to_list_postorder(self):
        node_list = []
        if self.left:
            node_list.extend(self.left.to_list_postorder())
        if self.right:
            node_list.extend(self.right.to_list_postorder())
        node_list.append(self.value)
        return node_list

    def copy(self):
        new_root = Node(self.value)
        if self.left:
            new_root.left = self.left.copy()
        if self.right:
            new_root.right = self.right.copy()
        return new_root

    def __del__(self):
        if self.left:
            del self.left
        if self.right:
            del self.right

    def to_string(self, level=0):
        TAB = "    "
        strings = []
        if self.left:
            strings.append(self.left.to_string(level+1))
        strings.append(TAB * level + " -> " + str(self.value))
        if self.right:
            strings.append(self.right.to_string(level+1))
        return "\n".join(strings)

    def __str__(self):
        return self.to_string()


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
print(tree.count())
print(tree.to_list_preorder())
print(tree.to_list_inorder())
print(tree.to_list_postorder())

