# Simple linked list
# with remove and re-defined exception


class Node:
    def __init__(self, value):
        """Polozku inicializujeme hodnotou value"""
        self.value = value
        self.next = None

    def __repr__(self):
        """Reprezentace objektu na Pythonovske konzoli"""
        return str(self.value)


class LinkedList:
    def __init__(self, values = None):
        """Spojovany seznam volitelne inicializujeme seznamem hodnot"""
        if values is None:
            self.head = None
            return
        self.head = Node(values.pop(0)) # pop vrati a odstrani hodnotu z values
        node = self.head
        for value in values:
            node.next = Node(value)
            node = node.next

    def __repr__(self):
        """Reprezentace na Pythonovske konzoli:
        Hodnoty spojene sipkami a na konci None"""
        values = []
        node = self.head
        while node is not None:
            values.append(str(node.value))
            node = node.next
        values.append("None")
        return " -> ".join(values)

    def __iter__(self):
        """Iterator prochazejici _hodnotami_ seznamu,
        napr. pro pouziti v cyklu for"""
        node = self.head
        while node is not None:
            yield node.value
            node = node.next

    def add_first(self, node):
        """Prida polozku na zacatek seznamu,
        tedy na head."""
        node.next = self.head
        self.head = node

    def add_last(self, node):
        """Prida polozku na konec seznamu."""
        p = self.head
        prev = None
        while p is not None:
            prev = p
            p = p.next
        prev.next = node

    def add_after(self, target_val, node):
        p = self.head
        while (p is not None) and (p.value != target_val):
            p = p.next
        if p is None:
            raise ValueError(f"{target_val=} not found in list.")
        else:
            node.next = p.next
            p.next = node

    def add_before(self, target_val, node):
        p = self.head
        if p.value == target_val: # hned prvni hodnota je hledana
            node.next = p
            self.head = node
            return
        while (p is not None) and (p.value != target_val):
            prev = p
            p = p.next
        if p is None:
            raise ValueError(f"{target_val=} not found in list.")
        else:
            node.next = p
            prev.next = node

    def remove_node(self, target_node_value):
        if self.head is None:
            raise ValueError("List is empty")

        if self.head.value == target_node_value:
            self.head = self.head.next
            return

        previous_node = self.head
        p = self.head.next
        while (p is not None) and (p.value != target_node_value):
            prev = p
            p = p.next
        if p is None:
            raise ValueError("Node with value '%s' not found" % target_node_value)
        prev.next = p.next
        del p

