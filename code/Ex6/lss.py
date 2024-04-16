
class Node:
    def __init__(self, value: int = None, next = None):
        self.value = value
        self.next = next

head = Node(0, 
            Node(1,
            Node(2,
            Node(3,
            Node(4
            )))))

p = head
while p:
    print(p.value)
    p = p.next