import sys
input = sys.stdin.readline

지구_답,태양_답,달_답 = map(int,input().split())
초기지구, 초기태양, 초기달, 답 = 1,1,1,1

while True:
    if 초기지구 == 지구_답 and 초기태양 == 태양_답 and 달_답 == 초기달:
        print(답)
        break
    else:
        초기지구 += 1
        초기태양 += 1
        초기달 += 1
        답 += 1
        if 초기지구 >= 16:
            초기지구 -= 15
        if 초기태양 >= 29:
            초기태양 -= 28
        if 초기달 >= 20:
            초기달 -= 19



