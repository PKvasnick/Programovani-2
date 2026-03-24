from doctest import testmod
from functools import cache, wraps


# Dekorátor, počítající počet volání funkce. Počet volání se ukládá jako atribut funkce inner.
# Toto není úplně dokonalá implementace, protože nepřenáší signaturu funkce f.
def counted(f):
    @wraps(f)
    def inner(*args, **kwargs):  # obecná signatura funkce f
        inner.calls += 1  # inkrementujeme atribut
        return f(*args, **kwargs)

    inner.calls = 0  # zřizujeme atribut funkce inner (ještě nebyla volána!)
    return inner


@counted  # namísto lev(...) pokaždé volej counted(lev)(...)
@cache
def lev(s: str, t: str) -> int:
    """Finds Levenshtein (edit) distance between two strings"""
    if (not s) or (not t):
        return len(s) + len(t)
    if s[0] == t[0]:
        return lev(s[1:], t[1:])
    return 1 + min(lev(s[1:], t), lev(s, t[1:]), lev(s[1:], t[1:]))


def main():

    s = "Démon kýs škaredý, chvost vlečúc po zemi"
    t = "ko mne sa priplazil, do ucha šepce mi:"

    k = min(len(s), len(t))
    print(
        lev(s[:k], t[:k]), lev.calls
    )  # i při volání atributu se namísto lev volá inner


if __name__ == "__main__":
    testmod()
    main()
