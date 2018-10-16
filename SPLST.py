# cook your code here
for t in range(input()):
    a, b, c, x, y = map(int, raw_input().split())
    if (x+y)!=(a+b+c):
        print "NO"
    else:
        if min(a,b,c)<=min(x,y):
            print "YES"
        else:
            print "NO"
