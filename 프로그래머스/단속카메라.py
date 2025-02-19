def solution(routes):
    routes = sorted(routes,key = lambda x : x[1])
    last_camera = -30001
    
    cnt = 0
    for s,e in routes:
        if (s > last_camera):
            last_camera = e
            cnt += 1
    
    return cnt