# Const class:
# Container for numbers protected against change
# Variant 1: frozen dataclass

from dataclasses import dataclass


@dataclass(frozen=True)
class ConstClass:
    PI: float = 3.1416
    E: float = 2.7183


def main() -> None:
    print(ConstClass.PI, ConstClass.E) # No need to create instance
    ConstClass.PI = 42 # dataclasses.FrozenInstanceError: cannot assign to field 'PI'


if __name__ == "__main__":
    main()