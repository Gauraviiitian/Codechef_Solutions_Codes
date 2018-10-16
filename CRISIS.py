# cook your code here

for t in range(input()):
    n, x = map(int, raw_input().split())
    s = [0]
    s.extend(map(int, raw_input().split()))
    c = [s[i]*i for i in range(n+1)]
    cpi = 0
    p = 0.0
    index = [0]*(n+1)
    index[0] = 1
    m = -1000000000
    while True:
        ind = 0
        m = -1000000000
        for i in range(1, n+1):
            if index[i]==1:
                continue
            if p!=0:
                val = (cpi+c[i])/(p+i) - cpi/p
            else:
                val = c[i]/i
            #print val
            if val>m:
                ind = i
                m = val
        if x>0 or m>0:
            p += ind
            index[ind] = 1
            cpi = cpi+c[ind]
            x -= 1
        else:
            break
    print cpi/p
