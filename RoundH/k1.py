# pass small test case

T = int(input())
for t in range(T):
    N = int(input())
    data = map(int, input().split())
    data = list(data)
    mapCount = dict()
    ans = [0]
    ptr = 0
    for i in data:
        ptr = ptr + 1
        i = int(i)
        if(i in mapCount):
            mapCount[i] = mapCount[i] + 1 
        else:
            mapCount[i] = 1
        
        # print(mapCount)
        c = 0
        ref = ans[-1] + 1
        for k,v in mapCount.items():
            if(k>=ref):
                c = c + v
        # print (c)
        if(c==0):
            ans.append(ref-1)
        elif (c<ref):
            ans.append(ref-1)
        else:
            ans.append(c)

    ans = ' '.join(map(str, ans[1:]))
    print("Case #{}: {}".format(t+1, ans))


    
