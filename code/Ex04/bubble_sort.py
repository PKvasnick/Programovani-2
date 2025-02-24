from bisect import bisect_left, bisect_right

data = [0, 11, 22, 33, 33, 44, 55, 55, 55]

for i in range(7):
    k = 10*i + i
    print(k, bisect_right(data, k) - bisect_left(data,k))
