num_to_bits=[0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4];  
  
# Recursively get nibble of a given number  
# and map them in the array 
def countSetBits(num): 
    nibble = 0; 
    if(0 == num): 
        return num_to_bits[0]; 
      
    # Find last nibble 
    nibble = num & 0xf; 
      
    # Use pre-stored values to find count 
    # in last nibble plus recursively add 
    # remaining nibbles. 
      
    return num_to_bits[nibble] + countSetBits(num >> 4);
    
def maxSubarrayXOR(arr,n): 
    ans = 0
    # Pick starting points of subarrays 
    for i in range(n): 
        # to store xor of current subarray 
        curr_xor = 0 
   
        # Pick ending points of 
        # subarrays starting with i 
        for j in range(i,n): 
          
            curr_xor = curr_xor ^ arr[j]
            setBits = countSetBits(curr_xor)
            if (setBits % 2 == 0):
                ans = max(ans, j-i+1)
                
    return ans

T = int(input())
for t in range(T):
    N, Q = map(int, input().split())
    A = [int(e) for e in  input().split()]
    ans = []
    for q in range(Q):
        i, v = map(int, input().split())
        A[i]=v
        ans.append (maxSubarrayXOR(A, N))
    submit = 'Case #' + str(t+1)+ ':'
    for a in ans:
        submit = submit + ' ' + str(a)
    print (submit)