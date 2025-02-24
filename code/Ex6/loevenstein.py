from functools import cache, lru_cache


# Dekorátor, počítající počet volání funkce
def counted(f):
    def inner(s, t):
        inner.calls += 1 # inkrementujeme atribut
        return f(s, t)
    inner.calls = 0 # zřizujeme atribut funkce inner
    return(inner)

@counted
@lru_cache(maxsize=100)
def lev(s:str, t:str) -> int:
    """Finds Levenshtein (edit) distance between two strings"""
    if (not s) or (not t):
        return len(s) + len(t)
    if s[0] == t[0]:
        return lev(s[1:], t[1:])
    return 1 + min(
        lev(s[1:], t),
        lev(s, t[1:]),
        lev(s[1:], t[1:])
    )


s = "Démon kýs škaredý, chvost vlečúc po zemi"
t = "ko mne sa priplazil, do ucha šepce mi:"

k = 12

print(lev(s[:k],t[:k]), lev.calls)