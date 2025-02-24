from functools import reduce
from sys import stdin


def read_from_console():
    for line in stdin.readlines():
        if "-1" in line:
            break
        yield float(line)
    return


maximum = reduce(max, read_from_console(), float("-inf"))
print(maximum)