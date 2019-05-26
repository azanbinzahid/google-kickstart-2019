import numpy

def maxRepeating(my_lst): 
    strr = ''.join(map(str, my_lst))
    l = len(strr) 
    count = 0
  
    # Find the maximum repeating  
    # character starting from strr[i] 
    res = strr[0] 
    for i in range(l): 
          
        cur_count = 1
        for j in range(i + 1, l): 
      
            if (strr[i] != strr[j]): 
                break
            cur_count += 1
  
        # Update result if required 
        if cur_count > count : 
            count = cur_count 
            res = strr[i] 
    return res, count 


def sub_lists(list1): 
  
    # store all the sublists  
    sublist = list()
      
    # first loop  
    for i in range(len(list1) + 1): 
          
        # second loop  
        for j in range(i + 1, len(list1) + 1): 
              
            # slice the subarray  
            sub = list1[i:j] 
            if(len(set(sub))==1 and len(sub)>1):
                sublist.append((i, len(sub))) 
      
    return sublist#sorted(sublist, key=lambda x: x[0])


for T in range(int(input())):
    R, C, K = map(int, input().split())
    
    # grid = numpy.zeros(shape=(R,C))
    grid = [[0] * C for _ in range(R)]
    
    for r in range(R):
        row = input().split()
        for c in range(C):
           grid[r][c] = row[c]

    ans = [[] for _ in range(C)]
    
    for row in grid:

        for i in sub_lists(row):
            start = i[0]
            length = i[1]
            ans[start].append (length) 
    p = -1

    for aa in ans:
        try:
            a, b = maxRepeating(aa)
            a = int(a)
            b = int (b)
            if (p < a*b):
                p = a*b
        except:
            pass
        
    print("Case #{}: {}".format(T+1, p))
        