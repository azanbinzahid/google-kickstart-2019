def getKey(item):
    return item[1] + item[2] * item[0]

def getKey1(item):
    return item[1] * item[2] 

def getKey2(item):
    return item[1]

def getKey3(item):
    return item[2]

def getKey4(item):
    return item[0]

def getKey5(item):
    return item[1] - item[2] * item[0]

def solve(keyFunc, data):
    data = sorted(data, key = keyFunc, reverse = True)
    ans = 0
    seconds_past = 0
    # print(data)
    for e in data:
        toAdd = e[1] - seconds_past*e[2]
        if (toAdd < 0 ):
            toAdd = 0
        ans = ans + toAdd
        seconds_past = seconds_past + e[0]

    return ans


T = int(input())
for t in range(T):
    N = int(input())
    data = []
    send = set()
    for n in range(N):
        S, E, L = map(int, input().split())
        data.append((S,E,L))
    
    send.add(solve(getKey, data))
    send.add(solve(getKey1, data))
    send.add(solve(getKey2, data))
    send.add(solve(getKey3, data))
    send.add(solve(getKey4, data))
    send.add(solve(getKey5, data))

    ans = max(send)

    print("Case #{}: {}".format(t+1, ans))