T = input()
for t in range(int(T)):
    N, S = map(int, input().split())
    E = []
    valid = 0
    for n in range(N):
        C = input().split()
        A = set()
        for i in range(int(C[0])):
            A.add(int(C[i+1]))
        E.append(A)
    for i in range(len(E)):
        for j in range(len(E)):
            j=j+i+1
            if(j==len(E)):
                break

            result =  all(elem in E[j]  for elem in E[i])
            result2 =  all(elem in E[i]  for elem in E[j])


            if not result or not result2:
                # print("check-->>", E[i], E[j])
                valid = valid+1
                if(not result and not result2):
                    valid = valid+1
    print("Case #{}: {}".format(t+1, valid))
