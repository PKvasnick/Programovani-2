# Nerekurzivni verze se zasobnikem

n = int(input())
mince = [int(s) for s in input().split()]
assert(len(mince) == n)
suma = int(input())

# Musíme obracet pořadí mincí, aby se nám vypisovali ve správném pořadí
stack = [[m] for m in reversed(mince)]
while stack:
    platba = stack.pop()
    curr_sum = suma - sum(platba)
    curr_mince = 0 if len(platba) == 0 else mince.index(platba[-1])
    for m in reversed(mince[curr_mince:]):
        if curr_sum - m > 0:
            stack.append([*platba, m])
        elif curr_sum - m == 0:
            print(*[*platba, m])