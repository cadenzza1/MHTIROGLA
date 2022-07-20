import sys
input = sys.stdin.readline

a,b = map(int,input().split())

a_set = list(map(int,input().split()))
b_set = list(map(int,input().split()))

a_set = set(a_set)
b_set = set(b_set)

a_without_b = a_set - b_set
b_without_a = b_set - a_set

print(len(a_without_b) + len(b_without_a))
