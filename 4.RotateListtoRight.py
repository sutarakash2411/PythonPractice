## Rotate a list to the right by k steps

myList = [12,13,53,35,87,44,76,97,35,92]

k = int(input("How many steps to move right?"))
k = k % len(myList)

#Logic1: Using list slicing
newList = []
newList = myList[-k:]+ myList[:-k]
print("NewList using slicing logic: ",newList)

#Logic2: Using collection deque
from collections import deque

dq = deque(myList)
dq.rotate(k)
rotated = list(dq)
print("New List updated using deque: ", rotated)