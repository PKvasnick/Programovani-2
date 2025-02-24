n = int(input())
vysledek = 0

def sgn(x):
    if x < 0:
        return -1
    elif x == 0:
        return 0
    else:
        return 1

while "=" not in (operator := str(input())):
    m = int(input())
    
    if "+" in operator:
        vysledek += n
        n = m
    
    if "-" in operator:
        vysledek += n
        n = -m
        
    if "*" in operator:
        n *= m
        
    if "/" in operator:
        n = sgn(x)(abs(x) // m)

        
vysledek += n
print(vysledek)