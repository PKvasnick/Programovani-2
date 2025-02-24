from itertools import product


W = 10
v = [10, 40, 30, 50]
w = [5, 4, 6, 3]


def generate_sets() -> set[frozenset[int]]:
    sets = set()
    for indices in product([0,1], repeat = len(w)):
        new_set = [i for i in range(len(w)) if indices[i]]
        new_w = sum(w[i] for i in new_set)
        if new_w > W:
            continue
        sets.add(frozenset(new_set))
    return sets


def main() -> None:
    sets = generate_sets()
    for s in sets:
        print(list(s), sum(v[i] for i in s), sum(w[i] for i in s))
    max_set = max(sets, key = lambda s: sum(v[i] for i in s))
    print(list(max_set))
    print(sum(v[i] for i in max_set))


if __name__ == "__main__":
    main()