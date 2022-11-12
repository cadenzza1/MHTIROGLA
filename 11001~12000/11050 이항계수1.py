import sys

input = sys.stdin.readline

def factorial(n):
    ans = 1
    for i in range(2,n+1):
        ans = ans * i
    return ans

def e_hang(n,k):
    return int(factorial(n) / factorial(k) / factorial(n-k))

n , k = map(int,input().split())

print(e_hang(n,k))