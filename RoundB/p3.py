def takeMax(array, S):
    ret = len(array)
    for s in set(array):
        c = array.count(s)
        if(c>S):
            ret = ret-c
    return ret

T = int(input())
for t in range(T):
    ans = []
    N, S = map(int, input().split())
    seq = input().split()
    m = len(set(seq)) * S

    for l in range(N):
        for r in range(N):
            if (abs(l-r)<m-S):
                continue
            apnd = takeMax(seq[l-1:r+1], S)
            if(apnd==m):
                ans.append(apnd)
                break
            ans.append(apnd)

    print("Case #{}: {}".format(t+1, max(ans)))