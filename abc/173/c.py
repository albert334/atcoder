import itertools
H,W,K = map(int, input().split())

matrix =[]
rowblack = []

for i in range(H):
    row = list(input())
    matrix.append(row)
    rowblack.append(row.count('#'))

allblacks = sum(rowblack)
ans = 0

selectRows = list(itertools.product([0,1], repeat=H))
selectColumns = list(itertools.product([0,1], repeat=W))

for selectRow in selectRows:
    for selectColumn in selectColumns:
        counter = 0

        for row in range(H):
            for column in range(W):
                if selectRow[row] == 0 and selectColumn[column] == 0 and matrix[row][column] == '#':
                    counter += 1
        
        if counter == K:
            ans += 1

print(ans)