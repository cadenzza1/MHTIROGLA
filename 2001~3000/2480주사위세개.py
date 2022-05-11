a,b,c = map(int,input().split())

num = (a,b,c)

if len(set(num)) == 1:

    print(10000 + a*1000)

elif len(set(num)) == 2:

    if a==b:

        print(1000 + 100*a)

    elif a==c:

        print(1000 + 100*a)

    elif b==c:

        print(1000 + 100*b)

else:

    print(100*max(num))