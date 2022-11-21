import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    sentence = list(input().split())
    for i in sentence:
        i = list(i)
        for j in range(len(i) // 2):
            i[j], i[len(i)-j-1] = i[len(i)-j-1], i[j]
        i = ''.join(i)
        print(i, end = ' ')
    print()
    