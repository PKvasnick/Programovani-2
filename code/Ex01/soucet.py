from itertools import zip_longest

# Sestrojíme slovník pro sčítání číslic
# Klíče: dvojice číslic (0-9). Hodnoty: dvojice (přenos, součet % 10
add_table = {(i, j) : divmod(i + j, 10) for i in range(10) for j in range(10)}

# Načteme dvě čísla jako seznamy číslic
a = [int(x) for x in input()]
b = [int(x) for x in input()]

reversed_result = []	# Dobré jméno (C) Dan Ransdorf
carry = 0
for da, db in zip_longest(reversed(a), reversed(b), fillvalue=0):
    carry_1, da = add_table[(da, carry)]
    carry_2, digit_sum = add_table[(da, db)]
    _, carry = add_table[(carry_1, carry_2)]
    reversed_result.append(digit_sum)
if carry > 0:
    reversed_result.append(carry)

a_print = "".join(map(str, a))
b_print = "".join(map(str, b))
result_print = "".join(map(str, reversed(reversed_result)))
print(f"{a_print} + {b_print} = {result_print}")
