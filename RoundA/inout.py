import sys


T = int(input())
for t in range (0, T):
    A, B = map(int, input().split())
    # print (A,B)
    N = int(input())
    for n in range (0, N):
        mid = (A + B)//2
        print (mid)
        sys.stdout.flush()
        response = str(input())
        if (response == 'WRONG_ANSWER'):
            sys.exit()
        elif (response == 'CORRECT'):
            break
        elif (response == 'TOO_SMALL'):
            A = mid
        elif (response == 'TOO_BIG'):
            B = mid