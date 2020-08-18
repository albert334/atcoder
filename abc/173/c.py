import itertools
H,W,K = map(int, input().split())
ans = 0
matrix =[]

for i in range(H):
    row = list(input())
    matrix.append(row)

# パターン列挙
selectRows = list(itertools.product([0,1], repeat=H))
selectColumns = list(itertools.product([0,1], repeat=W))

for selectRow in selectRows:
    for selectColumn in selectColumns:
        counter = 0
        for row in range(H):
            for column in range(W):
                # 赤く塗りつぶされない＆黒であった箇所を集計
                if selectRow[row] == 0 and selectColumn[column] == 0 and matrix[row][column] == '#':
                    counter += 1
        if counter == K:
            ans += 1

print(ans)