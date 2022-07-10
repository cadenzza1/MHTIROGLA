import sys

n = int(sys.stdin.readline())
arr = []

for i in range(n):
    tmp_x , tmp_y = map(int,sys.stdin.readline().split())
    arr.append([tmp_x,tmp_y])

arr.sort()

for x,y in arr:
    print(x,y)