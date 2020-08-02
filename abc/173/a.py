N = int(input())
pay = N // 1000
if N % 1000 != 0:
    pay += 1
ans = pay * 1000 - N
print(ans)