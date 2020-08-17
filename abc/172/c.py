N,M,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
SA = [0]
SB = [0]

for i in range(N):
    SA.append(A[i]+SA[i])
for i in range(M):
    SB.append(B[i]+SB[i])
ans, j = 0, M

for i in range(N+1):
    if SA[i] > K:
        break 
    while SA[i] + SB[j] > K:
        j -= 1
    ans = max(ans, i+j)

print(ans)