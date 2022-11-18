import sys
from collections import deque
import itertools

input = sys.stdin.readline

arr = deque()

for _ in range(9):
    arr.append(int(input()))

for i in itertools.combinations(arr,7):
    if sum(i) == 100:
        ans = sorted(i)
        for j in ans:
            print(j)
        exit()    

        