from collections import namedtuple

Point = namedtuple("Point", "x y")

point = Point(3, 4)

print(point)
print(point.x)
print(point.y)

Zamestnanec = namedtuple("Zamestnanec", "Jmeno Prijmeni Bydliste")

pepa = Zamestnanec("Josef", "Dobrovský", "Praha")

print(f"{pepa.Jmeno=} {pepa.Prijmeni=} {pepa.Bydliste=}")

print(hash(pepa))