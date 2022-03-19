n = int(input()) # 가지고 있는 숫자 카드의 개수
n_num = list(map(int,input().split()))
n_num.sort()

m = int(input())
m_num = list(map(int,input().split()))

n_len = len(n_num)

for i in range(m):
    left, right = 0, (n_len - 1)

    is_find = False

    while left <= right:
        mid = (left + right) // 2

        if m_num[i] == n_num[mid]:
            is_find = True
            print(n_num.count(m_num[i]), end = ' ') # 파이썬 내장함수인 count쓰면 시간초과 떠버림.
            break

        elif m_num[i] < n_num[mid]:
            right = mid -1
            continue

        elif m_num[i] > n_num[mid]:
            left = mid + 1
            continue

    if is_find == False:
        print(0, end= ' ')