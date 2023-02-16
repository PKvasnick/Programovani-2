import sys

a0 = input()
b0 = input()

if (not a0.isdigit()) or (not b0.isdigit()):
    print("Ocekavaji se cela cisla!")
    sys.exit()

a = [int(d) for d in reversed(a0)]
b = [int(d) for d in reversed(b0)]

delka = max(len(a), len(b)) + 1
a.extend([0] * (delka - len(a)))
b.extend([0] * (delka - len(b)))

soucet = []
prenos = 0
for d1, d2 in zip(a, b):
    ds = (d1 + d2 + prenos) % 10
    soucet.append(ds)
    prenos = (d1 + d2 + prenos) // 10

assert(prenos == 0)

konecna_delka = len(soucet)
while soucet[konecna_delka - 1] == 0:
    konecna_delka -= 1

str_soucet = reversed(list(map(str, soucet[:konecna_delka])))
print("".join(str_soucet))

print(int(a0) + int(b0))


