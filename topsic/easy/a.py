W, K, D = map(int,input().split())
maxlength = max(K, W-K)
if D >= maxlength:
    print("Yes")
else:
    print("No")