n = int(input()) # n값 입력받기
n_num = list(map(int,input().split())) # n개의 기준이 되는 숫자들 입력받기
n_num.sort() # 파이썬이 기본으로 제공하는 sort함수는 퀵소트라 시간복잡도가 O(nlogn)이다.

m = int(input()) # m값 입력받기
m_num = list(map(int,input().split())) # n의 수들과 비교할 m개의 수 입력받기

len_n = len(n_num)

for i in range(m): # m개의 수만큼 반복
    left, right = 0 , len_n - 1 # left는 0번 인덱스, right는 '배열 길이 -1' 로 초기화

    res = None

    while left <= right: # left 인덱스가 right 인덱스보다 작거나 같은동안 반복 / 같을때도 하는 이유는 1개 남았을때도 확인 해야하기 때문!
        mid = (left+right) // 2
        if m_num[i] == n_num[mid]:
            print(1)
            res = True
            break
        
        elif m_num[i] < n_num[mid]:
            right = mid - 1
            continue
        
        elif m_num[i] > n_num[mid]:
            left = mid + 1
            continue
    if res == None:
        print(0)





