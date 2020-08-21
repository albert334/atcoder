K  = int(input())
a = 0

for i in range(K):
    a = (10 * a + 7) % K
    if a % K == 0:
        print(i+1)
        exit()
    else:
        a %= K

print(-1)