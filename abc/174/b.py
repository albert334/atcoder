N,D = map(int,input().split())
ans = 0

for i in range(N):
    X,Y = map(int,input().split())
    distance = X ** 2 + Y ** 2
    if distance <= D ** 2:
        ans += 1

print(ans)