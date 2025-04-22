zahony = int(input().strip())

řešení = 0

def oseti(možnost = []):
    global řešení, zahony
    if len(možnost) == zahony:
        řešení += 1
    else:
        možnost.append(-1)
        for i in range(2):
            možnost[-1] = i
            if len(možnost) > 1 and možnost[-1] == 0 and možnost[-2] == 0:
                continue
            oseti(možnost)
        možnost.pop()

oseti()

print(řešení)