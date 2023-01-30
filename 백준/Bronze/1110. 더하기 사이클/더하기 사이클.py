import sys
input = sys.stdin.readline

N = input().rstrip()
c = 1

if int(N) < 10: # zfill()
    N = '0'+N[0]

first = N

while 1:
    num_sum = int(N[0]) + int(N[1])
    nf = N[-1] + str(num_sum)[-1]
    N = nf

    if N[0] == first[0] and N[1] == first[1]:
        break
    else:
        c += 1
print(c)
