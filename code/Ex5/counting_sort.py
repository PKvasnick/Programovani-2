from random import randint

def count_sort(b:list[int], rmax: int) -> list[int]:
    bins = [0] * rmax	# vytvoříme přihrádky
    # roztřídíme
    for elem in b:		
        bins[elem] += 1
    # kumulativní součty obsazeností
    for i in range(rmax):	
        if i==0:
            continue
        bins[i] += bins[i-1]
    # naplníme výsledné pole
    output = [0] * len(b)
    for i in reversed(range(len(b))):
        j = b[i]
        bins[j] -= 1
        output[bins[j]] = j
    return output


r = 10
data = [randint(0,r-1) for _ in range(100)]

print(*data)
print(*count_sort(data, r))