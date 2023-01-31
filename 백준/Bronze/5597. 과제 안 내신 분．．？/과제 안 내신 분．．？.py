B = []

for i in range(28):
    A = int(input())
    B.append(A)

for j in range(1, 31):
    try:
        B.index(j)
    except:
        print(j)