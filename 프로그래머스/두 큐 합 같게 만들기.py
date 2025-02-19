from collections import deque

def solution(queue1, queue2):
    q1, q2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(q1), sum(q2)
    tot = sum1 + sum2
    cnt = 0
    
    if max(queue1)>tot//2:
        return -1
    if max(queue2)>tot//2:
        return -1
    if tot%2 != 0:
        return -1
    
    for i in range(300000):
        if sum1 == sum2:
            return cnt
        elif sum1 > sum2:
            num = q1.popleft()
            q2.append(num)
            sum1 -= num
            sum2 += num
            cnt += 1
        elif sum2 > sum1:
            num = q2.popleft()
            q1.append(num)
            sum1 += num
            sum2 -= num
            cnt +=1
    
    return -1