# Const class:
# Container for numbers protected against change
# Variant 2: class with custom __setattr__ method:

class Const:
    def __setattr__(self, name, value):
        if hasattr(self, name):
            raise TypeError('cannot mutate constant')
        super().__setattr__(name, value)


def main() -> None:
    chem = Const()           # needs an instance
    chem.avogadro = 6.022e23

    physics = Const()
    physics.G = 6.673e-11
    physics.h = 6.626e-34

    chem.avogadro = 7 # TypeError: cannot mutate constant


if __name__ == '__main__':
    main()