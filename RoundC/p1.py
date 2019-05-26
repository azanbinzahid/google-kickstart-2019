import numpy

def solve():
    N, R, C, Sr, Sc = map(int, input().split()) 
    N_chars = input()
    Sr = Sr -1
    Sc = Sc -1

    grid = list()
    grid = numpy.zeros(shape=(R,C))
    # grid = [[False] * C for _ in range(R)]
    grid[Sr][Sc] = True

    for i in N_chars:
        if(i=="N"):
            Sr = Sr - 1
            while(grid[Sr][Sc]==True):
                Sr = Sr - 1
            grid[Sr][Sc] = True
        if(i=="E"):
            Sc = Sc +1
            while(grid[Sr][Sc]==True):
                Sc = Sc +1
            grid[Sr][Sc] = True

        if(i=="S"):
            Sr = Sr + 1
            while(grid[Sr][Sc]==True):
                Sr = Sr + 1
            grid[Sr][Sc] = True
        if(i=="W"):
            Sc = Sc - 1
            while(grid[Sr][Sc]==True):
                Sc = Sc - 1
            grid[Sr][Sc] = True
    
    # for r in range(R):
    #     del grid[r][:]
    # print (grid)

    return (Sr, Sc)


for T in range(int(input())):
    Sr, Sc = solve()
    print("Case #{}: {} {}".format(T+1, Sr+1, Sc+1))