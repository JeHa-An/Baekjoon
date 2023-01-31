num = []

for _ in range(10):
    e = int(input())
    num.append(e % 42)

print(len(set(num)))