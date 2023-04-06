class Const:
    def __setattr__(self, name, value):
        if hasattr(self, name):
            raise TypeError('cannot mutate constant')
        super().__setattr__(name, value)


chem = Const()    # potřebujeme instanci
chem.avogadro = 6.022e23

physics = Const()
physics.G = 6.673e-11
physics.h = 6.626e-34

chem.avogadro = 7 # TypeError: cannot mutate constant
