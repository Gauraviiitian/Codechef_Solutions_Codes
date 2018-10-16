# cook your code here
for t in range(input()):
    l, r = raw_input().split()
    l = int(l)
    r = int(r)
    c1 = l%10
    c2 = r%10
    l = l-c1
    r = r-c2
    count = ((r-l)/10)*3
    for i in range(c1):
        if i==2 or i==3 or i==9:
            count -= 1
    for i in range(c2+1):
        if i==2 or i==3 or i==9:
            count += 1
    print count
