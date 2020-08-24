N,X,T = map(int,input().split())

sets = N // X
if N % X != 0:
    sets += 1

print(T*sets)