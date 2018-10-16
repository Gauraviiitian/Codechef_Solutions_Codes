    # cook your code here
    n = int(raw_input())
    p1 = 0
    p2 = 0
    max = 0
    flag = 0
    t1 = 0
    t2 = 0
    while n>0:
        a, b =raw_input().split(" ")
        a = int(a)
        b = int(b)
        t1 = t1 + a
        t2 = t2 + b
        if t1>t2:
            p1 = t1 - t2
        elif t2>t1:
            p2 = t2 - t1
        if p1>max:
            flag = 1
            max = p1
        elif p2>max:
            flag = 2
            max = p2
        n = n-1
    if flag == 1:
        print 1, max
    elif flag == 2:
        print 2, max 
