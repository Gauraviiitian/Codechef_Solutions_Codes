for t in range(input()):
    a, b = map(int, raw_input().split())
    if (b==0 and a>0) or (b==1 and a>1):
        print "-1"
        continue
    elif a==b-1:
        print "1"
        continue
    elif a==b:
        print "0"
        continue
    a = bin(a)[2:]
    b = bin(b-1)[2:]
    count1_a = a.count('1')
    count1_b = b.count('1')
    if count1_a==count1_b:
        print "1"
    elif count1_a>count1_b:
        print "2"
    else:
        print count1_b-count1_a+1
