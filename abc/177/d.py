N, M = map(int, input().split())

# 行先記憶用
rooting = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    rooting[A].append(B)
    rooting[B].append(A)

# グループの最大人数
max_group_num = 1

# 到達判定フラグ（到達していれば1）
visited = [0 for _ in range(N+1)]

# 幅優先探索
for i in range(1, N+1):
    if  visited[i] == 1:
        continue
    visited[i] = 1
    queue = [i]
    group_num = 1

    while not queue == []:
        h = queue.pop(0)
        for n in rooting[h]:
            if visited[n] != 1:
                queue.append(n)
                group_num += 1
                visited[n] = 1

    max_group_num = max(max_group_num, group_num)

print(max_group_num)