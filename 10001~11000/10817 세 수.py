import sys

input = sys.stdin.readline

a,b,c = map(int,input().split())

arr = [a,b,c]
arr.remove(max(arr))
print(max(arr))