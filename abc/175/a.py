S = input()
ans = 0
for i in range(1,4):
    checking = "R" * i
    if checking in S:
        ans = i
print(ans)