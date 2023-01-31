T = int(input())

for i in range(T):
    c = 0
    res = 0
    ox = list(input())
    for j in ox:
        if j == 'O':
            res += (1 + c)
            c += 1
        else:
            c = 0
    print(res)
