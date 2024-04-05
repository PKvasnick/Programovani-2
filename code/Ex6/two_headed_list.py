# Double-headed linked list


class Node:
    def __init__(self, value):
        """Polozku inicializujeme hodnotou value"""
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        """Reprezentace objektu na Pythonovske konzoli"""
        return str(self.value)


class TwoHeadedList:
    def __init__(self, values=None):
        """Spojovany seznam volitelne inicializujeme seznamem hodnot"""
        if values is None:
            self.head = None
            self.tail = None
            return
        self.head = Node(values.pop(0))  # pop vrati a odstrani hodnotu z values
        node = self.head
        for value in values:
            node.next = Node(value)
            node.next.prev = node
            node = node.next
        self.tail = node

    def __repr__(self):
        """Reprezentace na Pythonovske konzoli:
        Hodnoty spojene sipkami a na konci None"""
        values = ["None"]
        node = self.head
        while node is not None:
            values.append(str(node.value))
            node = node.next
        values.append("None")
        return " <-> ".join(values)

    def __iter__(self):
        """Iterator prochazejici _hodnotami_ seznamu,
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

    def append(self, value):
        """Append value to head"""
        node = Node(value)
        node.next = self.head
        if self.head:
            self.head.prev = node
        self.head = node
        if not self.tail:
            self.tail = node

    def appendleft(self, value: int):
        """Append value to tail"""
        node = Node(value)
        node.prev = self.tail
        if self.tail:
            self.tail.next = node
        self.tail = node
        if not self.head:
            self.head = node

    def pop(self) -> int:
        """Pop from head side"""
        result = None
        if self.head:
            result = self.head.value
            self.head = self.head.next
            if not self.head:
                self.tail = None
        return result

    def popleft(self) -> int:
        """Pop from tail side"""
        result = None
        if self.tail:
            result = self.tail.value
            self.tail = self.tail.prev
            if not self.tail:
                self.head = None
            else:
                self.tail.next = None
        return result

    def __len__(self):
        count = 0
        for node in self:
            count += 1
        return count


from random import randint

def main() -> None:
    values = [randint(1,10) for _ in range(10)]
    print(values)
    queue = TwoHeadedList(values)
    print(queue)
    queue.appendleft(20)
    print(queue)
    queue.popleft()
    print(queue)
    queue.append(30)
    print(queue)
    queue.pop()
    print(queue)


if __name__ == "__main__":
    main()