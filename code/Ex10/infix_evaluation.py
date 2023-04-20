cisla = []
operatory = []
prioritky = {'+': 0, '-': 0, '*': 1, '/': 1}            #operacím přiřadíme priority, abychom rozlišili, které se provedou první

while True:
    vstup = input()
    if vstup ==  '=':                                   #znaménkem = výraz končí, končí tedy i naše načítání výrazu
        break
    
    if vstup.isdigit():                                 #čísla přiřadíme do příslušného seznamu
        cisla.append(int(vstup))                        #seznam také slouží jako takový zásobník, do kterého vkládáme a bereme prvky na konec
        
    else:
        while operatory and prioritky[operatory[-1]] >= prioritky[vstup]:       #pokud načteme znaménko s vyšší prioritou, vyhodnotíme ho hned
            znamenko = operatory.pop()
            b, a = cisla.pop(), cisla.pop()
            
            if znamenko == '+':
                cisla.append(a + b)
            elif znamenko == '-':
                cisla.append(a - b)
            elif znamenko == '*':
                cisla.append(a * b)
            elif znamenko == '/':
                cisla.append(a // b)
        
        operatory.append(vstup)                         #operátor přidáme do seznamu operátorů

while operatory:                                        #a vyhodnotíme zbylé operátory
    znamenko = operatory.pop()
    b, a = cisla.pop(), cisla.pop()
    
    if znamenko == '+':
        cisla.append(a + b)
    elif znamenko == '-':
        cisla.append(a - b)
    elif znamenko == '*':
        cisla.append(a * b)
    elif znamenko == '/':
        cisla.append(a // b)

print(cisla[0])                 #jediné zbylé číslo v seznamu je námi hledaný výsledek