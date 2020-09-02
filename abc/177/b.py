def check_same_sentence(big_str, small_str):
    num_b = len(big_str)
    num_s = len(small_str)
    ans = 0
    for i in range(num_b - num_s + 1):
        tmp = 0
        for j in range(num_s):
            if big_str[i+j] == small_str[j]:
                tmp += 1
        ans = max(ans, tmp)
    # 最大で何文字同じかを返す
    return ans

S = input()
T = input()

ans = check_same_sentence(S, T)
print(len(T)-ans)