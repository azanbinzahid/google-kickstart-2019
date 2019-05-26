T = int(input())
for t in range(T):
    num = int(input())
    N = list(str(num))

    for i,d in enumerate (N):
        if d == '4':
            N[i]='3'
    
    num1 = int(''.join(N))
    num2 = num-num1



    print('Case #{}: {} {}'.format(t+1, num1, num2))