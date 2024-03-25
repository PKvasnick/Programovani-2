# Vložení nové položky do setříděného seznamu

kam = [11, 22, 33, 44, 55, 66, 77, 88]
co = int(input())


def insort(co: int, kam: list[int]) -> list[int]:
    '''
    Zařadí hodnotu co na správné místo v setříděném seznamu kam
    '''

    l = 0
    if co < kam[l]:
        return [co] + kam
    p = len(kam) - 1
    if co > kam[p]:
        return kam + [co]

    while p - l > 1:
        stred = (l + p) // 2
        strval = kam[stred]
        if strval > co:
            p = stred  # Jdeme doprava
        else:
            l = stred  # Jdeme doleva

    return kam[:p] + [co] + kam[p:]

print(insort(co, kam))