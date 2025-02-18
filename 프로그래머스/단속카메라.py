def solution(routes):
    answer = -30001
    
    routes = sorted(routes,key = lambda x : x[1])
    
    cnt = 0
    for s,e in routes:
        if (s > answer):
            answer = e
            cnt += 1
    
    return cnt