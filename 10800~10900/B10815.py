#5
#6 3 2 10 -10
#8
#10 9 -5 2 3 4 5 -10

n = int(input())
n_num = list(map(int,input().split()))
n_num.sort()

m = int(input())
m_num = list(map(int,input().split()))

n_len = len(n_num)


for i in range(m):
    left , right = 0, (n_len - 1)

    res = None

    while left <= right:
        mid = (left + right) // 2

        if m_num[i] == n_num[mid]:
            print(1, end = ' ')
            res = True
            break

        elif m_num[i] < n_num[mid]:
            right = mid - 1
            continue
    
        elif m_num[i] > n_num[mid]:
            left = mid + 1
            continue

    if res != True:
        print(0, end = ' ')
    
