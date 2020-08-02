import numpy as np
N = int(input())
comfort = list(map(int,input().split()))
comfort_reverse = np.sort(comfort)[::-1]

ans = comfort_reverse[0]

if N > 2:
    for i in range(N-2):
        num = i // 2 + 1
        ans += comfort_reverse[num]

print(ans)