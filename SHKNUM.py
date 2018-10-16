for t in range(input()):
    n = input()
    #print n,
    if n==1:
        print "2"
        continue
    bn = bin(n)[2:]
    if bn.count("1")==1:
        print "1"
        continue
    if bn.count("1")==2:
        print "0"
        continue
    min_val = ""
    max_val = ""
    c = 0
    for i in range(len(bn)):
        if bn[i]=="1":
            c += 1
            min_val += "1"
        else:
            min_val += "0"
        if c==2:
            min_val += "0"*(len(bn)-i-1)
            break
    if bn[0:2]=="11":
        max_val = "1" + "0"*(len(bn)-1) + "1"
    else:
        for i in range(1, len(bn)):
            if bn[i]=="1":
                max_val = "1" + "0"*(i-2) + "1" + "0"*(len(bn)-i)
                break
    max_val = int(max_val, 2)
    min_val = int(min_val, 2)
    #print min_val, max_val,
    print min(n-min_val, max_val-n)
