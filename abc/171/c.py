N = int(input())
alphabet = list("abcdefghijklmnopqrstuvwxyz")
res = ""

while (N > 0):
    N -= 1
    num = int(N % 26)
    res += alphabet[num]
    N /= 26
    N = N // 1

print(res[::-1])