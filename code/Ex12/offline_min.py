import heapq


def main():
    data = input().strip().split()
    values = []
    heapq.heapify(values)
    for s in data:
        if "E" in s:
            print(heapq.heappop(values))
        else:
            heapq.heappush(values, int(s))


if __name__ == "__main__":
    main()
