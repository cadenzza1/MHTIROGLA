import sys
input = sys.stdin.readline

n, m = map(int,input().split())

poke_arr = {}
for i in range(1,n+1):
    tmp = input().rstrip()
    poke_arr[i] = tmp
    poke_arr[tmp] = i

quiz_arr = {}
for _ in range(m):
    quiz_arr[_] = input().rstrip()

for i in quiz_arr:
    if quiz_arr[i].isdigit():
        print(poke_arr[int(quiz_arr[i])])
    else:
        print(poke_arr[quiz_arr[i]])