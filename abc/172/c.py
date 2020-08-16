N,M,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

SA = [0]
SB = [0]

tmp_A, tmp_B = 0 ,0

for i in range(N):
    tmp_A += A[i]
    if tmp_A <= K:
        SA.append(tmp_A)
    else:
        break

for i in range(M):
    tmp_B += B[i]
    if tmp_B <= K:
        SB.append(tmp_B)
    else:
        break

ans = 0
cursol_B = len(SB) - 1

for i in range(len(SA)):
    while SA[i] + SB[cursol_B] > K:
        cursol_B -= 1
        
    ans = max(ans, i + cursol_B)

print(ans)