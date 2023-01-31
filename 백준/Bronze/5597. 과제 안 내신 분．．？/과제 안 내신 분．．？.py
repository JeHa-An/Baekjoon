B = []

for i in range(28):
    A = int(input())
    B.append(A)

for j in range(1, 31):
    if j not in B:
        print(j)