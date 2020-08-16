X, K, D = map(int,input().split())

if X == 0:
    if (K % 2 == 0):
        print(0)
    else:
        print(D)

    exit()

if X > 0:
    if X % D == 0:
        a = X // D
    else:
        a = X // D + 1

    if a > K:
        print(abs(X-K*D))
        exit()
    
    if K % 2 == 0:
        if a % 2 == 0:
            print(abs(X-a*D))
        else:
            print(abs(X-a*D+D))
    else:
        if a % 2 == 0:
            print(abs(X-a*D+D))
        else:
            print(abs(X-a*D))
        exit()

if X < 0:
    if X % D == 0:
        a = -1 * X // D
    else:
        a = -1 * X // D + 1

    if a > K:
        print(abs(X+K*D))
        exit()
    
    if K % 2 == 0:
        if a % 2 == 0:
            print(abs(X+a*D))
        else:
            print(abs(X+a*D-D))
    else:
        if a % 2 == 0:
            print(abs(X+a*D-D))
        else:
            print(abs(X+a*D))
        exit()