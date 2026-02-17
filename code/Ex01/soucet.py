from itertools import zip_longest

# Sestrojíme slovník pro sčítání číslic
# Klíče: dvojice číslic (0-9). Hodnoty: dvojice (přenos, součet % 10)
add_table = {(i, j): divmod(i + j, 10) for i in range(10) for j in range(10)}

# Načteme dvě čísla jako seznamy číslic
a = [int(x) for x in input()]
b = [int(x) for x in input()]

result_reversed = []
carry = 0
for da, db in zip_longest(reversed(a), reversed(b), fillvalue=0):
    carry1, sum_temp = add_table[(da, db)]
    carry2, sum_final = add_table[(sum_temp, carry)]
    result_reversed.append(sum_final)
    _, carry = add_table[(carry1, carry2)]

if carry > 0:
    result_reversed.append(carry)

a_print = "".join(map(str, a))
b_print = "".join(map(str, b))
result_print = "".join(map(str, reversed(result_reversed)))
print(f"{a_print} + {b_print} = {result_print}")
