H,W = map(int,input().split())
Ch, Cw = map(int,input().split())
Dh, Dw = map(int,input().split())
S = [list(input()) for _ in range(H)]

INF = H * W

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

# def steppable(h,w):
#     if not (h in range(H)) or not (w in range(W)):
#         return False
#     if S[h][w] == '#':
#         return False
#     else:
#         return True

num_step = [[INF for w in range(W)] for h in range(H)]
num_step[Ch - 1][Cw - 1] = 0

# スタート地点を定義
queue = [(Ch - 1, Cw - 1)]
num_warp = 0

# 幅優先探索
while not queue == []:
    magic_tiles = []
    while not queue == []:
        h = queue.pop(0) # here 
        if h[0] == Dh - 1 and h[1] == Dw - 1:
            print(num_warp)
            exit()
        # next_  = [
        #     (h[0] + 1, h[1], 0),
        #     (h[0] - 1, h[1], 0),
        #     (h[0], h[1] + 1, 0),
        #     (h[0], h[1] - 1, 0),]
        for i in range(4):
            if 0 <= h[0]+dy[i] < H and 0 <= h[1]+dx[i] < W and S[h[0]+dy[i]][h[1]+dx[i]] == '.' \
                 and num_step[h[0]+dy[i]][h[1]+dx[i]] > num_warp:
                queue.append((h[0]+dy[i], h[1]+dx[i]))
                num_step[h[0]+dy[i]][h[1]+dx[i]] = num_warp

        # 魔法を使っていける場所を検討
        mx = [-2, -1 , 0, 1, 2]
        my = [-2, -1 , 0, 1, 2]

        for x in mx:
            for y in my:
                 if 0 <= h[0] + y < H and 0 <= h[1] + x < W and S[h[0] + y][h[1] + x] == '.' \
                     and num_step[h[0] + y][h[1] + x] == INF:
                    magic_tiles.append((h[0] + y, h[1] + x))

    num_warp += 1

    # キューの追加
    for magic in magic_tiles:
        if num_step[magic[0]][magic[1]] == INF:
            num_step[magic[0]][magic[1]] == num_warp
            queue.append((magic[0], magic[1]))

print(-1)