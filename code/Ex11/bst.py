# Binary search tree class


class BSTnode:
    def __init__(self, value = None, prev = None, left = None, right = None):
        self.value = value
        self.prev = prev
        self.left = left
        self.right = right

    def insert(self, value):
        if value > self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTnode(value, self, None, None)
        else:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTnode(value, self, None, None)

    def to_string(self, level):
        strings = []
        if self.left:
            strings.append(self.left.to_string(level + 1))
        strings.append(" " * 4 * level + "->" + str(self.value))
        if self.right:
            strings.append(self.right.to_string(level + 1))
        return "\n".join(strings)

    def __repr__(self):
        return self.to_string(level = 0)

    def to_list_inorder(self):
        values = []
        if self.left:
            values.extend(self.left.to_list_inorder())
        values.append(self.value)
        if self.right:
            values.extend(self.right.to_list_inorder())
        return values

    def find(self, value):
        if self.value == value:
            return self
        if self.value < value:
            if self.right:
                return self.right.find(value)
        else:
            if self.left:
                return self.left.find(value)
        return None

    def depth(self):
        left_depth = 1
        if self.left:
            left_depth += self.left.depth()
        right_depth = 1
        if self.right:
            right_depth += self.right.depth()
        return max(left_depth, right_depth)

    def asymmetry(self):
        left_depth = 0
        if self.left:
            left_depth = self.left.depth()
        right_depth = 0
        if self.right:
            right_depth = self.right.depth()
        return right_depth - left_depth

    def rotate(self):
        new_tree = self.right
        new_tree.insert(self.value)
        print(new_tree)
        print(new_tree.asymmetry())
        return new_tree


def main() -> None:
    vals = [3, 6, 5, 2, 1, 8, 4, 9, 7, 0]
    tree = BSTnode(vals.pop())
    for val in vals:
        tree.insert(val)
    print(tree)
    print(tree.to_list_inorder())
    print(tree.find(11))
    print(tree.depth())
    print(tree.asymmetry())
    tree = tree.rotate()
    print(tree)
    print(tree.depth())
    print(tree.asymmetry())
    print(tree.to_list_inorder())


if __name__ == '__main__':
    main()