import sys
from functools import reduce

a0 = input()
b0 = input()

if (not a0.isdigit()) or (not b0.isdigit()):
    print("Ocekavaji se cela cisla!")
    sys.exit()

delka = max(len(a0), len(b0)) + 1
a0 = a0.zfill(delka)
b0 = b0.zfill(delka)

a = [int(d) for d in reversed(a0)]
b = [int(d) for d in reversed(b0)]

def transform(state, pair):
    '''Transformuje stav state = (prenos, vysledek) pomoci novych cislic
    (d1, d2) na novy stav'''
    soucet = (pair[0] + pair[1] + state[0]) % 10
    state[1].append(soucet)
    prenos = (pair[0] + pair[1] + state[0]) // 10
    return prenos, state[1]


prenos, soucet = reduce(transform, zip(a, b), (0, []))

assert(prenos == 0)

konecna_delka = len(soucet)
while soucet[konecna_delka - 1] == 0:
    konecna_delka -= 1

print(*reversed(soucet[:konecna_delka]), sep = "")

# Kontrola
print(int(a0) + int(b0))


