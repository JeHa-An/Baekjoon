c = int(input())

for _ in range(c):
    n = list(map(int, input().split()))
    avg = 0

    for i in range(1, n[0]+1):
        avg += n[i]

    avg = avg / n[0]

    c = 0
    for j in range(1, n[0]+1):
        if n[j] > avg:
            c += 1
    out = round(c / n[0] * 100, 3)
    print("%0.3f%%" % (out))