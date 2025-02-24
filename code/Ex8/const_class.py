# Const class:
# Container for numbers protected against change
# Variant 1: frozen dataclass

from dataclasses import dataclass


@dataclass(frozen=True)
class ConstClass:
    PI: float = 3.1416
    E: float = 2.7183


ConstClass.EULER_GAMMA = 0.57722 # Can add attributes to class
ConstClass.E = 2.71828 # Can modify class attributes

const = ConstClass()   # Instances are frozen - no adding/modifying
print(const.PI, const.E)


const.PI = 42 # dataclasses.FrozenInstanceError: cannot assign to field 'PI'
