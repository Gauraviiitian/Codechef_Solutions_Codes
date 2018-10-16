for t in range(input()):
    a = raw_input()
    b = raw_input()
    c1 = []
    c2 = []
    for i in range(3):
        if a[i]=="b" or b[i]=="b":
            c1.append(i)
        if a[i]=="o" or b[i]=="o":
            c2.append(i)
    if len(c1)==2 and len(set(c2)-set(c1))>=1:
        print "yes"
    elif len(c1)==3 and len(c2)>=1:
        print "yes"
    else:
        print "no"
