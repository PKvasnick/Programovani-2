from contextlib import suppress

with suppress(EOFError):
    while p := input():
        print(int(p))