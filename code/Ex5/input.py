from sys import stdin

cisla = []
with stdin as vstup:
    for line in vstup:
        if "-end-" in line:
            break
        cisla.append(int(line.strip()))

print(cisla)
