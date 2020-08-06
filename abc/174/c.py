K  = int(input())
a = 0

for i in range(K+1):
    a += 7 * (10 ** i)
    if a % K == 0:
        print(i+1)
        exit()

print(-1)