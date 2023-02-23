m = int(input("zadej modul:"))

lines = []
lines.append("graph TD;\n")

for r in range(m):
    lines.append(f"{r} --> {(10*r) % m};\n")

with open("mermaid_graph.txt", "w") as infile:
    for line in lines:
        infile.write(line)

print("Done.")