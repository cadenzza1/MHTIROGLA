a, b, c = map(int,input().split())
# 판매비용 > 고정비용 + 가변비용
# a = 고정비용 b = 가변비용 c = 노트북 가격
# 노트북 판매 개수가 중요한거네.

if b>=c:
    print(-1)
else:
    print(int(a//(c-b)+1))