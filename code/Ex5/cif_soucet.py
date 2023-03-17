def cif_soucet_1(cislo: int) -> int:
    """mod 10 dává číslici, div 10 zbytek"""
    soucet = 0
    while cislo:
        soucet += cislo % 10
        cislo //= 10
    return soucet

def cif_soucet_2(cislo: int) -> int:
    return sum(map(int, str(cislo)))

def cif_soucet_3(cislo: int) -> int:
    """mod 10 dává číslici, div 10 zbytek"""
    soucet = 0
    while cislo:
        cislo, zbytek = divmod(cislo, 10)
        soucet += zbytek
    return soucet