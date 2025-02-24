from functools import reduce

a0 = [int(c) for c in input()]
b0 = [int(c) for c in input()]

delka = max(len(a0), len(b0)) + 1
a0 = a0.zfill(delka)
b0 = b0.zfill(delka)


def transform(stav, cislice):
    seznam, prenos = stav
    soucet = cislice[0] + cislice[1] + prenos
    seznam.append(soucet % 10)
    prenos = soucet // 10
    return seznam, prenos


rev_soucet, prenos = reduce(transform, zip(reversed(a0), reversed(b0)), ([], 0))

assert (prenos == 0)

if rev_soucet[-1] == 0:
    rev_soucet.pop()

print(*reversed(rev_soucet), sep="")
print("Kontrola:")
print(int(a0) + int(b0))
