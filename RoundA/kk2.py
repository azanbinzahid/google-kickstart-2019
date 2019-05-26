import sys

def delTime(x,y,new_grid):
    if (grid[x][y]):
        return 0
    else:
        mini = pow(2,64)
        for i in range(R):
            for j in range(C):
                if (new_grid[i][j]==1):
                    s = abs(x-i) + abs (y-j)
                    mini = s if mini > s else mini
        return mini 
        

def overall(new_grid):
    max_time = -1
    for l in new_grid:
        max_time=max(l) if max_time<max(l) else max_time
    return max_time

def distGrid(new_grid):
    dist_grid = [[0 for x in range(C)] for y in range(R)] 
    for r in range(R):
        for c in range(C):
            dist_grid[r][c] = delTime(r,c,new_grid)
    return(overall(dist_grid))

T = int(input())
for t in range(T):
    zero_loc = []
    R, C = map(int, input().split())
    seqR = []
    for r in range(R):
        seqR.append(input())
    grid = [[0 for x in range(C)] for y in range(R)] 
    for r in range(R):
        for c in range(C):
            grid[r][c] = int(seqR[r][c])
            if (grid[r][c]==0):
                zero_loc.append([r,c])

    orig = grid
    mini = distGrid(grid)
    for z in zero_loc:
        new_grid = orig
        new_grid[z[0]][z[1]] = 1
        # print(new_grid)
        val = distGrid(new_grid)
        mini = val if mini > val else mini
        new_grid[z[0]][z[1]] = 0
    print ('Case #' + str(t+1)+ ':', mini)