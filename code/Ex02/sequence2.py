from functools import reduce

def read_from_console():
    while "-1" not in (line := input()):
        yield float(line)
    return


maximum = reduce(max, read_from_console(), float("-inf"))
print(maximum)