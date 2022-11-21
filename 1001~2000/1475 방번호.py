cards = list(map(int,input())) # 숫자별로 리스트화
cnt = [ 1 for _ in range(10) ]# count 테이블 생성. 
ans = 1 # 필요한 세트 개수

for i in cards:
    if i != 6 and i != 9:
        cnt[i] -= 1
        if cnt[i] == -1:
            ans += 1
            for l in range(10):
                cnt[l] += 1
    elif i == 6 or i == 9:
        if cnt[i] == 0:
            if i == 6:
                if cnt[9] != 0:
                    cnt[9] -= 1
                else:
                    cnt[i] -= 1
                    ans += 1
                    for l in range(10):
                        cnt[l] += 1
            elif i == 9:
                if cnt[6] != 0:
                    cnt[6] -= 1
                else:
                    cnt[i] -= 1
                    ans += 1
                    for l in range(10):
                        cnt[l] += 1
        else:
            cnt[i] -= 1
print(ans)

# cnt테이블은 최초 1로 초기화
# for문을 이용하여 한 숫자씩 받아들이기.
# cnt[i] -= 1
# if 받아온 수가 6도 아니고 9도 아님: ( 일반적인 경우 )
#   if 감소시켰는데 그 값이 0이라면:
#       ans값 1증가시키고 
#       cnt테이블 전체 1씩 증가
# elif 받아온 수가 6또는 9면:
#   if cnt[i] == 0:
#       if i == 6:
#           if cnt[9] != 0:
#               cnt[9] -= 1
#           else:
#               ans += 1
#               for l in range(10):
#                   cnt[l] += 1
#       elif i == 9:
#           if cnt[6] != 0:
#               cnt[6] -= 1
#           else:
#               ans += 1
#               for l in range(10):
#                   cnt[l] += 1