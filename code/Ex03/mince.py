# Rekurzivni verze - backtracking

n = int(input())
mince = [int(x) for x in input().split()]
assert(len(mince) == n)
suma = int(input())

platba = []


def zkus(suma: int, max_mince: int = 0) -> None:
    """Zkusi pridat některou minci k seznamu platba.
    Pokud nelze přidat, buď vytiskne anebo neudělá nic."""
    for m in mince[max_mince:]:
        platba.append(m)
        if suma - m > 0:
            zkus(suma - m, mince.index(m))
        elif suma - m == 0:
            print(*platba)
        platba.pop()


zkus(suma, 0)
