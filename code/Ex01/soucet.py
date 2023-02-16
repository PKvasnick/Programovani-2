# Hodne neucesana verze, na hodine jsme nestihli upravit do pekne podoby

a = [int(x) for x in input()]
b = [int(x) for x in input()]

if a > b:
    a,b = b,a
a = list(reversed(a))
b = list(reversed(b))

prebytek = 0
c = []
for i in range(len(a)):
    vysledek = a[i] + b[i] + prebytek
    c.append(vysledek % 10)
    prebytek = vysledek // 10
    
if (len(b) > len(a)):
    c.append(prebytek + b[len(a)])
elif (prebytek > 0):
    c.append(prebytek)

for i in range(len(a) + 1, len(b)):
    c.append(b[i])

print("".join([str(x) for x in reversed(c)]))

