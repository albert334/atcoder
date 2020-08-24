N = int(input())
A = list(map(int, input().split()))
Q = int(input())
BCs = [list(map(int,input().split())) for _ in range(Q)]
max_A = max(A)

# Aの値について数列を作る
# A_num = [A.count(i) for i in range(10 ** 5 + 1)]

A_num = [0 for i in range(10 ** 5 + 1)]
for a in A:
    A_num[a] += 1

Si = sum(A)

for BC in BCs:
    # BC[0] ...　置換前の値
    # BC[1] ...　置換後の値
    
    if A_num[BC[0]] > 0: 
        Si += A_num[BC[0]] * (BC[1] -BC[0])
        A_num[BC[1]] += A_num[BC[0]]
        A_num[BC[0]] = 0

    print(Si)