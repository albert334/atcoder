N, M = map(int,input().split())
flag = [0 for i in range(M+1)]

for i in range(1, N+1):
    a, b = map(int,input().split())
    t = a + b

    if t + 1 <= i <= t + M:
        flag[i-t] = 1

print(sum(flag))