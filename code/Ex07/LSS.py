# Operations on a headless simply linked list


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

    def __iter__(self):
        """Iterator traversing the list's nodes, can be used in a for cycle."""
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def get_last(self):
        for node in self:
            pass
        return node

    def __len__(self):
        count = 0
        for node in self:
            count += 1
        return count

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def append_left(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            return None
        new_end = None
        popped_node = self.head
        while popped_node.next is not None:
            new_end = popped_node
            popped_node = popped_node.next
        if new_end is None:
            self.head = None
        else:
            new_end.next = None
        return popped_node

    def pop_left(self):
        if self.head is None:
            return None
        popped_node = self.head
        self.head = self.head.next
        return popped_node.data

    def remove(self, key):
        current_node = self.head
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return
        prev_node = None
        while current_node and current_node.data != key:
            prev_node = current_node
            current_node = current_node.next
        if current_node is None:
            return
        prev_node.next = current_node.next
        current_node = None

    def pop_node(self, key):
        current_node = self.head
        if current_node and current_node.data == key:
            self.head = current_node.next
            return current_node
        prev_node = None
        while current_node and current_node.data != key:
            prev_node = current_node
            current_node = current_node.next
        if current_node is None:
            return None
        prev_node.next = current_node.next
        return current_node

    def __del__(self):
        current_node = self.head
        while current_node:
            next_node = current_node.next
            del current_node
            current_node = next_node

    def swap_with_next(self, node: Node):
        if node == self.head and self.head.next is not None:
            self.head = self.head.next
            node.next = self.head.next
            self.head.next = node
            return

        prev_node = self.head
        while prev_node.next and prev_node.next != node:
            prev_node = prev_node.next
        if prev_node.next is None:  # node is not found
            return
        # prev -> node -> next_node to prev -> next_node -> node
        next_node = node.next
        prev_node.next = next_node
        node.next = next_node.next
        next_node.next = node

    def sort(self):
        if self.head is None or self.head.next is None:
            return
        current_node = self.head
        n_swaps = -1
        while n_swaps != 0:
            n_swaps = 0
            current_node = self.head
            while current_node and current_node.next:
                next_node = current_node.next
                if current_node.data > next_node.data:
                    self.swap_with_next(current_node)
                    n_swaps += 1
                else:
                    current_node = current_node.next

    def invert(self):
        prev_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node

    def partition(self, unary_predicate):
        # Partition the list based on the unary predicate, i.e.,
        # a function up(x) -> bool. The nodes that satisfy the predicate
        # are moved to the front of the list, preserving their relative order.
        less_head = less_tail = None
        greater_head = greater_tail = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            if unary_predicate(current_node.data):
                if less_head is None:
                    less_head = less_tail = current_node
                else:
                    less_tail.next = current_node
                    less_tail = current_node
                less_tail.next = None
            else:
                if greater_head is None:
                    greater_head = greater_tail = current_node
                else:
                    greater_tail.next = current_node
                    greater_tail = current_node
                greater_tail.next = None
            current_node = next_node
        if less_head is None:
            self.head = greater_head
        else:
            self.head = less_head
            less_tail.next = greater_head


def main():
    llist = LinkedList()
    llist.append(3)
    llist.append(2)
    llist.append(1)
    llist.print_list()
    llist.append_left(4)
    llist.append_left(5)
    llist.print_list()
    llist.swap_with_next(llist.head.next)
    llist.print_list()
    llist.remove(llist.head.next.data)
    llist.print_list()
    llist.sort()
    llist.print_list()
    llist.invert()
    llist.print_list()
    llist.partition(lambda x: x % 2 == 0)
    llist.print_list()


if __name__ == "__main__":
    main()
