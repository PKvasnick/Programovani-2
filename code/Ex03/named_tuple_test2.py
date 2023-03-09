from typing import NamedTuple

class Point(NamedTuple):
    x : int
    y : int

point = Point(4, 5)
print(point.x, point.y)
print(point[0], point[1])