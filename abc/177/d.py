N, M = map(int, input().split())
numbering = [-1 for i in range(N+1)]
numbering[1] = 1

for _ in range(M):
    AB = list(map(int, input().split()))

print(AB)