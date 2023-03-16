from timeit import Timer

def cif_soucet_1(cislo: int) -> int:
    """mod 10 dává číslici, div 10 zbytek"""
    soucet = 0
    while cislo:
        soucet += cislo % 10
        cislo //= 10
    return soucet

def cif_soucet_2(cislo: int) -> int:
    return sum(map(int, str(cislo)))


t1 = Timer("cif_soucet_1(123456789)", "from speedy import cif_soucet_1")
print(1, t1.timeit(number = 1000000))

t2 = Timer("cif_soucet_2(123456789)", "from speedy import cif_soucet_2")
print(2, t2.timeit(number = 1000000))
