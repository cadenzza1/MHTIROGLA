import sys
input = sys.stdin.readline

def x_small(x,w):
    if x <= w-x:
        return x
    else:
        return (w-x)

def y_small(y,h):
    if y <= h-y:
        return y
    else:
        return (h-y)

x,y,w,h = map(int,input().split())

if x_small(x,w) <= y_small(y,h):
    print(x_small(x,w))
else:
    print(y_small(y,h))