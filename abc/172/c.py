N,M,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

Ai = max_A = max_SA = 0
Bi = max_B = max_SB = 0

for i in range(N):
    if Ai + A[i] <= K:
        Ai += A[i]
        max_SA = Ai
        max_A = i    
    else:
        break


for i in range(M):
    if Bi + B[i] <= K:
        Bi += B[i]
        max_SB = Bi
        max_B = i    
    else:
        break

# 局所探索でより効率的な解がないかを探す
cursol_A = max_A
cursol_B = 0
tmp_K = max_SA
ans = max_A + 1

# cursol_B = 0 でどこまで動かせるか
tmp = 0
for j in range(max_B):
    if tmp_K + B[j] <= K:
        tmp_K += B[j]
        tmp += 1
    else:
        break

cursol_B = tmp
ans = max(ans, ans + cursol_B)

# cursol_B > 0でAを1個ずつ減らしていってどれだけ増分できるか
for i in range(cursol_A, -1, -1):
    tmp_K -= A[i]
    # cursol_Bをどこまで進められるか
    tmp = 0
    for j in range(cursol_B, max_B+1):
        if tmp_K + B[j] <= K:
            tmp_K += B[j]
            tmp += 1
        else:
            break
        
    ans = max(ans, ans + tmp -1)
    cursol_B = min(max_B, cursol_B + tmp)

print(ans)