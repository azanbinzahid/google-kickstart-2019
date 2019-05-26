T = int(input())
for t in range(T):
    N = int(input())
    P = input()
    # grid = [[0 for _ in range(N)] for _ in range(N)]
    paths = []
    paths.append([0,0])
    for p in P:
        curr = paths[-1]
        if(p=='S'):
            paths.append([curr[0]+1, curr[1]])
        elif(p=='E'):
            paths.append([curr[0], curr[1]+1])
    
    # paths = path[]
    
    myPath = []
    currMy = [0,0]
    for p in P:
        if p == 'E':
            if ([currMy[0],currMy[1]+1] in paths and currMy in paths):
                myPath.append('S')
                myPath.append('E')
                currMy = [currMy[0]+1,currMy[1]+1]
            
            else:
                if (currMy[1]+1==N and [currMy[0]+1,currMy[1]+1 in paths] ):
                    if (currMy in paths):
                        if ([currMy[0]+1,currMy[1]] in paths):
                            myPath.append('E')
                            myPath.append('S') 
                        else:
                            myPath.append('S')
                            myPath.append('E')
                    else:
                        myPath.append('S')
                        myPath.append('E')
                    currMy = [currMy[0]+1,currMy[1]+1]
                else:
                    myPath.append('E')
                    currMy = [currMy[0],currMy[1]+1]
        if p == 'S':
    
            if ([currMy[0]+1,currMy[1]] in paths and currMy in paths):
                myPath.append('E')
                myPath.append('S')
                currMy = [currMy[0]+1,currMy[1]+1]
            
            else:
                if (currMy[0]+1==N and [currMy[0]+1,currMy[1]+1 in paths] ):
                    if (currMy in paths):
                        if ([currMy[0],currMy[1]+1] in paths):
                            myPath.append('S')
                            myPath.append('E') 
                        else:
                            myPath.append('E')
                            myPath.append('S')
                            
                    else:   
                        myPath.append('E')
                        myPath.append('S')
                    currMy = [currMy[0]+1,currMy[1]+1]
                else:
                    myPath.append('S')
                    currMy = [currMy[0]+1,currMy[1]]
        
        
    ans = ''.join(myPath[:len(P)])
    
    print('Case #{}: {}'.format(t+1, ans))
