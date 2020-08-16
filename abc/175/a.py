S = list(input())
ans = 0
tmp = 0

for i in S:
    if i == 'R':
        tmp += 1
    else:
        tmp = 0
    ans = max(ans,tmp)

print(ans)