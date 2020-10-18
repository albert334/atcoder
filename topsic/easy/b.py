ans = list("AtCoder")
reversed_ans = list("aTcODER")

S = list(input())
flag = 0

for i in range(len(S)):
    if S[i] == ans[i]:
        continue
    elif S[i] == reversed_ans[i]:
        flag = 1
        continue
    else:
        print("No")
        exit()

if flag == 1:
    print("Maybe")
else:
    print("Yes")