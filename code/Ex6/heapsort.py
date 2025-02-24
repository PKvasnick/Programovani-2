# simplistic heap implementation
from random import randint


def print_heap(h: list[int], size: int) -> None:
    """Infix printout"""
    def to_string(h: list[int], index: int, size: int, level: int) -> list[str]:
        rows = []
        if (child := 2*index + 1) < size:
            rows.extend(to_string(h, child, size, level + 1))
        rows.append(f"{' '*(level * 4)} -- {h[index]}")
        if (child := 2*index + 2) < size:
            rows.extend(to_string(h, child, size, level + 1))
        return rows

    print("\n".join(to_string(h, 0, size, 0)))


def heapify(h:list[int]) -> None:
    """Turn a list into a max-heap in-place"""
    for element in range(len(h)):
        p = element
        while (prev := (p-1) // 2) >= 0:
            if h[p] > h[prev]:
                h[p], h[prev] = h[prev], h[p]
                p = prev
            else:
                break
        print_heap(h, element+1)
        print(h[element+1:])


def heap_sort(h: list[int]) -> None:
    """Turne a heap into a sorted list"""
    for heap_size in reversed(range(1, len(h))):
        h[0], h[heap_size] = h[heap_size], h[0]
        p = 0
        while True:
            p_child = 2 * p + 1
            if p_child >= heap_size:
                break
            p_child2 = 2 * p + 2
            if p_child2 < heap_size and h[p_child2] > h[p_child]:
                p_child = p_child2
            if h[p] >= h[p_child]:
                break
            h[p], h[p_child] = h[p_child], h[p]
            p = p_child
        print_heap(h, heap_size)
        print(h[heap_size:])


def main() -> None:
    heap = [randint(1,100) for _ in range(10)]
    print(heap)
    heapify(heap)
    print(heap)
    heap_sort(heap)
    print(heap)


if __name__ == '__main__':
    main()