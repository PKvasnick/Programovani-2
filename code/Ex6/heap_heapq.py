# Python3 program to demonstrate working of heapq

from heapq import heapify, heappush, heappop
from random import randint

# Creating empty heap
heap = []
heapify(heap)

# Adding items to the heap using heappush function
for i in range(10):
    heappush(heap, randint(1,100))

# printing the value of minimum element
print("Head value of heap : " + str(heap[0]))

# printing the elements of the heap
print("The heap elements : ")
for i in heap:
    print(i, end=' ')
print("\n")

element = heappop(heap)

# printing the elements of the heap
print("The heap elements : ")
for i in heap:
    print(i, end=' ')
print()

print()
print("Sorted elements:")
while heap:
    print(heappop(heap), end = " ")
print()