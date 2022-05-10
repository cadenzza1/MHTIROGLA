A,B = map(int,input().split())
C = int(input())

D = B+C
cnt = 0

if D >= 60:
    cnt = D // 60
    B = D % 60
    E = cnt + A
    if E >= 24:
        A = E-24
    else:
        A = A+cnt
else:
    A,B = A,D
print(A,B)