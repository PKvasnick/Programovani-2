from bisect import bisect_left

kde = [11, 22, 33, 44, 55, 66, 77, 88]
co = int(input())

poloha = bisect_left(kde, co)
print(poloha)
if kde[poloha] == co:
    print("Nalezeno v poloze ", poloha)
else:
    print("Nenalezeno")
