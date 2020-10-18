N = int(input())
S = list(input())

# 偶数
if N % 2 == 0:
    rest_even = N // 2
    rest_odd = N // 2
    next_L = 1
    next_R = N

    for i in S:
        if i == 'L':
            if rest_odd > 0:
                print(next_L)
                next_L += 2
                rest_odd -= 1

                if rest_odd == 0:
                    next_L = 2
            
            else:
                if rest_even > 0:
                    print(next_L)
                    next_L += 2
                    rest_even -= 1

        if i == 'R':
            if rest_even > 0:
                print(next_R)
                next_R -= 2
                rest_even -= 1

                if rest_even == 0:
                    next_R = N-1
            
            else:
                if rest_odd > 0:
                    print(next_R)
                    next_R -= 2
                    rest_odd -= 1

    exit()

# 奇数
rest_even = N // 2
rest_odd = N // 2 + 1

next_L = 1
next_R = N

for i in S:
    if i == 'L':
        if rest_odd > 0:
            print(next_L)
            next_L += 2
            rest_odd -= 1

            if rest_odd == 0:
                next_L = 2
                next_R = N-1
            
        else:
            if rest_even > 0:
                print(next_L)
                next_L += 2
                rest_even -= 1

    if i == 'R':
        if rest_odd > 0:
            print(next_R)
            next_R -= 2
            rest_odd -= 1

            if rest_odd == 0:
                next_L = 2
                next_R = N-1
            
        else:
            if rest_even > 0:
                print(next_R)
                next_R -= 2
                rest_even -= 1
 
