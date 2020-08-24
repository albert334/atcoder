N = list(input())
sum_N = 0
for i in range(len(N)):
    sum_N += int(N[i])

if sum_N % 9 == 0:
    print("Yes")
else:
    print("No")