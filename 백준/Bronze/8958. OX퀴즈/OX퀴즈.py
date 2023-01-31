T = int(input())
c = 0
res = 0
for i in range(T):
    ox = list(input())
    for j in ox:
        if j == 'O':
            res += (1 + c)
            c += 1
        else:
            c = 0
    print(res)
    res = 0
    c = 0