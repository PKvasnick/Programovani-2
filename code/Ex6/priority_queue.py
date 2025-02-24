from random import randint
from typing import NamedTuple


class PrioritizedItem(NamedTuple):
    priority: int
    value: int


def data_reader():
    for _ in range(10):
        priority = randint(0,10)
        value = randint(1000, 9999)
        yield PrioritizedItem(priority, value)
    return


class PriorityQueue:
    def __init__(self):
        self.heap = []

    def to_string(self, index: int, size: int, level: int) -> list[str]:
        rows = []
        size = len(self.heap)
        if (child := 2*index + 1) < size:
            rows.extend(to_string(h, child, size, level + 1))
        rows.append(f"{' '*(level * 4)} -- {h[index]}")
        if (child := 2*index + 2) < size:
            rows.extend(to_string(h, child, size, level + 1))
        return rows

    def __str__(self):


