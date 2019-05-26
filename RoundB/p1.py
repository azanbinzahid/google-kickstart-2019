def check(st) : 
  
    count = [0] * (256) 
    for i in range( 0, len(st)) : 
        count[ord(st[i])] = count[ord(st[i])] + 1
  
    # Count odd occurring characters 
    odd = 0
      
    for i in range(0, 256 ) : 
        if (count[i] & 1) : 
            odd = odd + 1
  
        if (odd > 1) : 
            return False
              
    # Return true if odd count is 0 or 1,  
    return True

T = int(input())
for t in range(T):
    ans = 0
    N, Q = map(int, input().split())
    Blocks = input()
    Qs = []
    for q in range(Q):
        l, r = map(int, input().split())
        test = Blocks[l-1:r]
        ans = ans + 1 if check(test) else ans
    


    print("Case #{}: {}".format(t+1, ans))