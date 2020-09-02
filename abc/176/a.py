def calc(N,X,T):
    sets = N // X
    if N % X != 0:
        sets += 1
    return T * sets

if __name__ == "__main__":
    N, X, T = map(int,input().split())
    ans = calc(N,X,T)
    print(ans)