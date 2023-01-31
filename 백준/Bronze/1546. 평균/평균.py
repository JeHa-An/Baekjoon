import sys
input = sys.stdin.readline

N = int(input())
M = list(map(int, input().split()))
M_max = max(M)
hap = 0

for i in M:
    res = i/M_max*100
    hap += res
print(hap/N)