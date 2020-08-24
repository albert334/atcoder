N = int(input())
A = list(map(int,input().split()))

if N == 1:
    print(0)
    exit()

ans = 0

for i in range(1,N):
    if A[i] < A[i-1]:
        ans += A[i-1] - A[i]
        A[i] = A[i-1]

print(ans)