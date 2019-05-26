import math
T = int(input())
for t in range(T):
    N = int(input())
    cc = 1
    while(True):    
        cc = cc + 1
        n = N/cc
        a = math.ceil(n) 
        b = N - a
        
        checka = str (a)
        checkb = str (b)


        if (a+b == N):
            if ('4' in checka or '4' in checkb):
                continue
            A = a;
            B = b;
            break

        a = math.floor(n) 
        b = N-a

        checka = str (a)
        checkb = str (b)

        if ( a + b == N):
            if ('4' in checka or '4' in checkb):
                    continue
            A = a;
            B = b;
            break

    print('Case #{}: {} {}'.format(t, A, B))