from contextlib import suppress

lst = list(range(10))

i = -1
with suppress(ValueError):
    i = lst.index(12)

print(i)

try:
    i = lst.index(12)
except ValueError:
    i = -2

print(i)