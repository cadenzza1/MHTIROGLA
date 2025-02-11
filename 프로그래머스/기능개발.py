from collections import deque

def solution(progresses, speeds):
    # 문제를 읽자마자 무선 '우선순위 큐'가 가장 먼저 떠올랐다.
    # 파이썬이 제공하는 deque가 필요해 보인다.
    # 가장 왼쪽에 있는 작업이 끝나야 뒤에 있는 작업이 완료된 것들도 배포될 수 있다.
    # 즉, 후방에 있는 것들이 아무리 빨리 작업이 끝나도 무조건 가장 왼쪽에 있는 친구가 완료되어야 배포 가능
    # 오히려 '큐'보다는 '스택'쪽에 가까운 문제인 듯 싶다.
    
    progresses = deque(progresses)
    speeds = deque(speeds)
    
    answer = []
    
    while(len(progresses)>=1):
        for i in range(len(progresses)): # 프로그램 개발하기
            progresses[i] += speeds[i]
        
        if progresses[0]>=100:
            cnt = 1
            progresses.popleft()
            speeds.popleft()
            while(len(progresses)>=1 and progresses[0] >= 100): # 가장 우선 순위가 높은 작업이 완료되면(100이 되면)
                cnt += 1
                progresses.popleft()
                speeds.popleft()
            answer.append(cnt)
                
    return answer