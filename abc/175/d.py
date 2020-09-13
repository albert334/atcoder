N, K = map(int, input().split())
moves = [0] + list(map(int, input().split()))
points = [0] + list(map(int, input().split()))
INF = 10**10
 
answer = -INF
for start in range(1, N+1):
    circle = [start]
    # 次のマス
    next = moves[start]

    # 1サイクルの得点
    c_score = points[start]
    
    # ループになるまで回し続ける
    while(next != start):
        circle.append(next)
        c_score += points[next]
        # ネクストを更新
        next = moves[next]

    # K回以下で得られる得点の最大値
    m_score = 0

    for i in range(min(len(circle), K)):
        # ループの切片
        m_score += points[circle[i]]
        # ループの回数
        loop_cnt = (K-i-1)//len(circle)
        # 更新
        answer = max(answer, m_score + max(0, loop_cnt * c_score))
print(answer)

# 計算回数がN*Nなので十分間に合う