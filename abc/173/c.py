H,W,K = map(int, input().split())
ans = 0
board =[list(input()) for _ in range(H)]

for paint_H in range(2 ** H): #行の塗りつぶし方の全列挙
    for paint_W in range(2 ** W): #列の塗りつぶし方の全列挙
        cnt = 0
        for i in range(H):
            for j in range(W):
                if (paint_H>>i)&1==0 and (paint_W>>j)&1==0:
                    if board[i][j] == '#':
                        cnt += 1
        if cnt == K:
            ans += 1
print(ans)