n = int(input())
n_nums = list(map(int,input().split()))

m = int(input())
m_nums = list(map(int,input().split()))

cards = {}
for i in n_nums:
    if i in cards:
        cards[i] += 1
    else:
        cards[i] = 1

for j in m_nums:
    if j in cards:
        print(cards[j], end = ' ')
    else:
        print(0, end = ' ')