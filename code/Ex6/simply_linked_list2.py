# Simple linked list


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
        """Iterator prochazejici polozkami seznamu,
        napr. pro pouziti v cyklu for"""
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def values(self):
        vals = []
        for node in self:
            vals.append(node.value)
        return vals

    def get_last_node(self):
        for node in self:
            pass
        return node

    def __len__(self):
        count = 0
        for node in self:
            count += 1
        return count

    def add_first(self, val):
        """Prida polozku na zacatek seznamu,
        tedy na head."""
        node = Node(val)
        node.next = self.head
        self.head = node

    def add_last(self, val):
        """Prida polozku na konec seznamu."""
        for p in self:
            pass
        node = Node(val)
        p.next = node

    def get_node(self, target_val):
        for p in self:
            if p.value == target_val:
                return p
        else:
            return None

    def add_after(self, target_val, new_val):
        p = self.get_node(target_val)
        if p is None:
            raise ValueError(f"{target_val} se nenachazi v seznamu.")
        node = Node(new_val)
        node.next = p.next
        p.next = node

    def add_before(self, target_val, new_val):
        if self.head.value == target_val:
            node = Node(new_val)
            node.next = self.head
            self.head = node
            return
        prev = self.head
        p = prev.next
        while (p is not None) and (p.value != target_val):
            prev = p
            p = p.next
        if p is None:
            raise ValueError(f"{target_val} se nenachazi v seznamu.")
        node = Node(new_val)
        node.next = p
        prev.next = node

    def remove(self, target_val):
        p = self.head
        if p.value == target_val:
            self.head = p.next
            del p
            return
        prev = p
        p = p.next
        while (p is not None) and (p.value != target_val):
            prev = p
            p = p.next
        if p is None:
            raise ValueError(f"{target_val} se nenachazi v seznamu.")
        prev.next = p.next
        del p


