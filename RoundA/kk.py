T = int(input())
for t in range(T):
    N, P = map(int, input().split())
    integers = [int(e) for e in  input().split()]
    integers.sort()
    integers = integers[::-1]
    cost_ans = []
    for n in integers:
        cost = 0
        ans = []
        for p in integers:
            if(p<=n):
                cost = cost + n - p
                ans.append(p)
                if(len(ans)==P):
                    break
        cost_ans.append([cost, ans])
    final = []
    for a in cost_ans:
        print (a)
        if len(a[1])==P:
            final.append(a[0])

    final.sort()

    print ('Case #' + str(t+1)+ ':', final[0])