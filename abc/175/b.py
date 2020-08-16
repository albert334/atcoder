def triangle(a, b, c):
    return (a + b > c and b + c > a and c + a > b)

def differ_num(a,b,c):
    return not (a == b or b == c or c == a)

N = int(input())
L = list(map(int,input().split()))
ans = 0

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1 ,N):
            if triangle(L[i],L[j],L[k]) and differ_num(L[i],L[j],L[k]):
                ans += 1

print(ans)