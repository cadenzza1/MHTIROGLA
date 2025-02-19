def solution(prices):
    answer = []
    
    # for문으로 prices 순회한다.
    # 찝은 수로부터 i값 1씩 증가시키면서 더 작은 값 나올 때까지 while문 돌린다.
    # cnt 변수 이용해서 더 작은 값의 index - i 해서 스택에 넣는다.
    
    for i, num in enumerate(prices):
        next = i + 1
        while next < (len(prices)-1) and prices[next] >= prices[i]:
            next += 1
        answer.append(next-i)
    
    answer[-1] = 0
        
    return answer