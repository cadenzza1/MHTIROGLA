H,M = map(int,input().split())

if M-45 < 0:
    if H == 0:
        H,M = 23,15+M
    else:
        H,M = H-1,15+M
else:
    H,M = H,M-45

print(H,M)