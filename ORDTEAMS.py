# cook your dish here
for t in range(input()):
    a = map(float, raw_input().split())
    b = map(float, raw_input().split())
    c = map(float, raw_input().split())
    
    if a==b or b==c or c==a:
        print "no"
        continue
    
    dif_ab = [a[0]/b[0], a[1]/b[1], a[2]/b[2]]
    dif_cb = [c[0]/b[0], c[1]/b[1], c[2]/b[2]]
    dif_ac = [a[0]/c[0], a[1]/c[1], a[2]/c[2]]
    f=1
    
    
    if dif_ab[0]>1:
        if dif_ab[1]<1 or dif_ab[2]<1:
            f = 0
    elif dif_ab[1]>1:
        if dif_ab[0]<1 or dif_ab[2]<1:
            f = 0
    elif dif_ab[2]>1:
        if dif_ab[1]<1 or dif_ab[0]<1:
            f = 0
    elif dif_ab[0]<1:
        if dif_ab[1]>1 or dif_ab[2]>1:
            f = 0
    elif dif_ab[1]<1:
        if dif_ab[0]>1 or dif_ab[2]>1:
            f = 0
    elif dif_ab[2]<1:
        if dif_ab[1]>1 or dif_ab[0]>1:
            f = 0
        
    if dif_cb[0]>1:
        if dif_cb[1]<1 or dif_cb[2]<1:
            f = 0
    elif dif_cb[1]>1:
        if dif_cb[0]<1 or dif_cb[2]<1:
            f = 0
    elif dif_cb[2]>1:
        if dif_cb[1]<1 or dif_cb[0]<1:
            f = 0
    elif dif_cb[0]<1:
        if dif_cb[1]>1 or dif_cb[2]>1:
            f = 0
    elif dif_cb[1]<1:
        if dif_cb[0]>1 or dif_cb[2]>1:
            f = 0
    elif dif_cb[2]<1:
        if dif_cb[1]>1 or dif_cb[0]>1:
            f = 0
    
    if dif_ac[0]>1:
        if dif_ac[1]<1 or dif_ac[2]<1:
            f = 0
    elif dif_ac[1]>1:
        if dif_ac[0]<1 or dif_ac[2]<1:
            f = 0
    elif dif_ac[2]>1:
        if dif_ac[1]<1 or dif_ac[0]<1:
            f = 0
    elif dif_ac[0]<1:
        if dif_ac[1]>1 or dif_ac[2]>1:
            f = 0
    elif dif_ac[1]<1:
        if dif_ac[0]>1 or dif_ac[2]>1:
            f = 0
    elif dif_ac[2]<1:
        if dif_ac[1]>1 or dif_ac[0]>1:
            f = 0
    
    if f==0:
        print "no"
    else:
        print "yes"
