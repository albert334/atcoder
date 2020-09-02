H,W = map(int,input().split())
Ch, Cw = map(int,input().split())
Dh, Dw = map(int,input().split())
S = [list(input()) for _ in range(H)]

INF = H * W

def steppable(h,w):
    if not (h in range(H)) or not (w in range(W)):
        return False
    if S[h][w] == '#':
        return False
    else:
        return True

num_step = [[INF for w in range(W)] for h in range(H)]
num_step[Ch - 1][Cw - 1] = 0

# スタート地点を定義
queue = [(Ch - 1, Cw - 1)]

# 幅優先探索
while not queue == []:
    h = queue.pop(0) # here
    next_  = [
        (h[0] + 1, h[1], 0),
        (h[0] - 1, h[1], 0),
        (h[0], h[1] + 1, 0),
        (h[0], h[1] - 1, 0),]

    for n in next_:
        if steppable(n[0], n[1]) and num_step[n[0]][n[1]] == INF:
            queue.append(n)
            num_step[n[0]][n[1]] = 0

if num_step[Dh - 1][Dw - 1] == 0:
    print(0)
    exit()

# マジックを検討
# スタート地点を定義
queue = [(Ch - 1, Cw - 1)]
magic_num = INF // 2 

while True:
    # 幅優先探索
    while not queue == []:
        h = queue.pop(0) # here
        next_  = [
            (h[0] + 1, h[1], 0),
            (h[0] - 1, h[1], 0),
            (h[0], h[1] + 1, 0),
            (h[0], h[1] - 1, 0),]

        for n in next_:
            if steppable(n[0], n[1]) and num_step[n[0]][n[1]] == magic_num:
                queue.append(n)
                num_step[n[0]][n[1]] = 0
    
    if num_step[Dh - 1][Dw - 1] == magic_num:
