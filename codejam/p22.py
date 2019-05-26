T = int(input())
for t in range(T):
    N = int(input())
    P = input()
    grid = [[1 for _ in range(N)] for _ in range(N)]
    paths = []
    paths.append([0,0])
    for p in P:
        curr = paths[-1]
        if(p=='S'):
            paths.append([curr[0]+1, curr[1]])
        elif(p=='E'):
            paths.append([curr[0], curr[1]+1])
    
    # paths = paths[1:-1]
    
    myPath = []
    currMy = [0,0]
    for p in P:


        Epath = [currMy[0],currMy[1]+1]
        Spath = [currMy[0]+1,currMy[1]]
        Diag =  [currMy[0]+1,currMy[1]+1]
       
        if p=='E':
            if(currMy in paths and Epath in paths):
                currMy = Diag;
                myPath.append('S')
                myPath.append('E')
            else:
                if (currMy in paths and Epath in paths and Diag in paths):
                    currMy = Spath
                    myPath.append('S')
                else:
                    currMy = Epath
                    myPath.append('E')



        elif p=='S':
            if(currMy in paths and Spath in paths):
                currMy = Diag;
                myPath.append('E')
                myPath.append('S')
            else:
                if (currMy in paths and Spath in paths and Diag in paths):
                    currMy = Epath
                    myPath.append('E')
                else:
                    currMy = Spath;
                    myPath.append('S')





    ans = str(''.join(myPath))
    
    print('Case #{}: {}'.format(t+1, ans))
