from doctest import testmod


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

    k = 13
    print(lev(s[:k], t[:k]))


if __name__ == "__main__":
    testmod()
    main()
