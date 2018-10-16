# cook your code here
for t in range(input()):
    s = raw_input()
    count = 0
    f = 0
    d1 = {'c', 'h', 'e', 'f'}
    for i in range(len(s)-3):
        d2 = {s[i], s[i+1], s[i+2], s[i+3]}
        if d1==d2:
            f=1
            count += 1
    if f==1:
        print "lovely", count
    else:
        print "normal"
