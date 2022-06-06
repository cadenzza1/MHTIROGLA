word = input()

dict = {
    'ABC' : 3,
    'DEF' : 4,
    'GHI' : 5,
    'JKL' : 6,
    'MNO' : 7,
    'PQRS' : 8,
    'TUV' : 9,
    'WXYZ' : 10
}

res = 0

for i in word:
    for key, val in dict.items():
        if i in key:
            res += val

print(res)