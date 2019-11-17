# correct answers but memory limit exceeded


import itertools

T = int(input())
for t in range(T):
    N = 9
    digit = []
    ans = "NO"
    data = map(int, input().split())
    data = list(data)
    for i in range(N):
        if(data[i]!=0):
            for _ in range(data[i]):
                digit.append(i+1)

    sum = 0
    for i in range(len(digit)):
        if(i % 2 == 0):
            sum = sum + digit[i]
        else:
            sum = sum - digit[i]
    
    if(sum == 0 or sum % 11 == 0):
        ans = "YES"

    if (ans != "YES"):
        perm = itertools.permutations(digit)  
        for li in list(perm):
            # print(li)
            sum = 0
            for i in range(len(li)):
                if(i % 2 == 0):
                    sum = sum + li[i]
                else:
                    sum = sum - li[i]
            if(sum == 0 or sum % 11 == 0):
                ans = "YES"
                break

    print("Case #{}: {}".format(t+1, ans))
