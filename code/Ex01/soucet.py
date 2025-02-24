# Hodne neucesana verze, na hodine jsme nestihli upravit do pekne podoby

a = [int(x) for x in input()]
b = [int(x) for x in input()]

if a > b:
    a,b = b,a
a = list(reversed(a))
b = list(reversed(b))

prenos = 0
c = []
for i in range(len(a)):
    vysledek = a[i] + b[i] + prenos
    c.append(vysledek % 10)
    prenos = vysledek // 10
    
if (len(b) > len(a)):
    c.append(prenos + b[len(a)])
elif (prenos > 0):
    c.append(prenos)

for i in range(len(a) + 1, len(b)):
    c.append(b[i])

print("".join([str(x) for x in reversed(c)]))

