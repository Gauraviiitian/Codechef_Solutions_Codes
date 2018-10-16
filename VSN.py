# cook your code here
for t in range(input()):
    st = map(float, raw_input().split())
    p = st[:3]
    q = st[3:6]
    d = st[6:9]
    c = st[9:12]
    r = st[12]
    m = (c[0]-p[0])*(q[0]-p[0]) + (c[1]-p[1])*(q[1]-p[1]) + (c[2]-p[2])*(q[2]-p[2])
    n = (c[0]-p[0])*d[0] + (c[1]-p[1])*d[1] + (c[2]-p[2])*d[2]
    k = (p[0] - c[0])**2 + (p[1] - c[1])**2 +(p[2] - c[2])**2 - r**2
    #print m, n, k
    a = n**2 - k*(d[0]**2 + d[1]**2 + d[2]**2)
    b = 2*m*n - 2*k*((q[0] - p[0])*d[0] + (q[1] - p[1])*d[1] + (q[2] - p[2])*d[2])
    c = m**2 - k*((q[0] - p[0])**2 + (q[1] - p[1])**2 + (q[2] - p[2])**2)
    #print a, b, c
    if a==0:
        time = -c/b
        print time
    else:
        time = [(-b - (b**2 - 4*a*c)**0.5)/(2*a), (-b + (b**2 - 4*a*c)**0.5)/(2*a)]
        if time[0]<=0:
            print time[1]
        elif time[1]<=0:
            print time[0]
        else:
            print min(time)
