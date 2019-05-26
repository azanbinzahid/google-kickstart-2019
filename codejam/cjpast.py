import math

def calculate(string):
    damage = 1
    final = 0
    for x in string:
        if (x=='C'):
            damage = damage * 2;
        elif (x=='S'):
            final = final + damage
    return final

T = int(input())
for t in range(T):
    put, put2 = map (str, input().split())
    D = int(put)
    P = put2
    ch = 0
    flag = 0
    l = math.factorial(len(P))
    while(calculate(P)>D):
        man = list(P)
        for i,c in enumerate(P):
            if (i+1 == len(P)): break
            if P[i]=='C' and P[i+1] == 'S':
                man[i]='S'
                man[i+1]='C'
                break
        P = ''.join(man)
        # print (P)
        ch = ch + 1
        if ch>l:
            flag = 1
            break

    if(flag):
        print('Case {}: {}'.format(t, 'IMPOSSIBLE'))
    else:
        print('Case {}: {}'.format(t, ch))