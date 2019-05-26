from itertools import permutations 

T = int(input())
for t in range(T):
    N, Q = map(int, input().split())
    bookings = []
    for q in range(Q):
        L, R = map(int, input().split())
        bookings.append([L,R])
    perm = permutations(bookings)
    # print (list(perm))
    all_cust = []
    for p in list(perm):
        # for each order order
        # for b in p:
        #     print (b)
        booked = []
        customer_given = []
        for i, rq in enumerate(p):
            customer_given.append(0)
            for r in range(rq[0],rq[1]+1):
                if (r in booked):
                    pass
                else:
                    booked.append(r)
                    customer_given[i]+=customer_given[i]+1
                    if (len(booked)==N): break
        all_cust.append(min(customer_given))
    print ('Case #' + str(t+1)+ ':', max(all_cust))