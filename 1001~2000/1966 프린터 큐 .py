from collections import deque

for _ in range(int(input())):
    cnt = 0
    # n과 m을 입력받는다.
    n,m = map(int,input().split())
    # pri라는 deque객체를 만들어서 중요도를 입력받는다.
    pri = deque(list(map(int,input().split())))
    #출력되는 값이 target값인지 확인하기 위한 idx리스트를 만든다.
    idx = deque(range(n))
    # 알고싶은 값의 인덱스를 target으로 설정해준다.
    idx[m] = 'target'

    while True:
        if pri[0] == max(pri):
            cnt += 1
            if idx[0] == 'target':
                print(cnt)
                break
            else:
                pri.popleft()
                idx.popleft()
        else:
            pri.rotate(-1)
            idx.rotate(-1)