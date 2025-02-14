def solution(name):
    
    alpha_move = 0
    cursor_move = len(name) - 1
    
    # Pseudo Code
    
    # for(name 한 글자씩 순회하기)
    # 뽑은 알파벳이 A로부터 정방향으로 가는 것이 빠른지, 역방향으로 가는 것이 빠른지 체크
    # 정방향 or 역방향으로 움직인 만큼 answer값에 플러스해주기
    # for문 끝나면 answer에 정답 값이 들어있으므로 answer 리턴해주면 끝
    
    # 결국 뽑은 알파벳이 A로부터 정방향으로 가는 것이 빠른지, 역방향으로 가는 것이 빠른지 체크 <-- 이게 핵심
    # 딕셔너리? 배열? 힙? 큐? 스택? 데크?
    # 어떤 자료구조를 택한 후 MIN(정방향으로 갔을 때의 이동 횟수, 역방향으로 갔을 때의 이동 횟수)를 answer에 더해주면 됨
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
             'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    
    for i, alpha in enumerate(name):
        right_ward = alphabet.index(alpha) # 정방향으로 갔을 때의 이동 횟수
        # 왜냐하면 결국 시작 알파벳인 A의 인덱스는 0이므로 
        alpha_move += min(right_ward,26-right_ward) # 정방향 이동 횟수, 역방향 이동 횟수 중 작은 값을 answer에 더한다.
        
        next = i+1
        while next < len(name) and name[next] == 'A':
            next += 1
            
        # 기존, 연속된 A의 왼쪽시작 방식, 연속된 A의 오른쪽시작 방식 비교 및 갱신
        cursor_move = min(cursor_move, 2 * i + len(name) - next, i + 2 * (len(name) -next))
    
    return alpha_move + cursor_move