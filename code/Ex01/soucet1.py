from functools import reduce

a0 = input()
b0 = input()

delka = max(len(a0), len(b0)) + 1
a0 = a0.zfill(delka)
b0 = b0.zfill(delka)

def transform(stav, cislice):
    soucet = int(cislice[0]) + int(cislice[1]) + stav[1]
    seznam = stav[0] + [soucet % 10]
    prenos = soucet // 10
    return seznam, prenos

rev_soucet, prenos = reduce(transform, zip(reversed(a0), reversed(b0)), ([], 0))

assert(prenos == 0)

if rev_soucet[-1] == 0:
    rev_soucet = rev_soucet[:-1]

print(*reversed(rev_soucet), sep = "")
print(int(a0) + int(b0))



