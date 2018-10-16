for t in range(input()):
    a, b, c = map(int, raw_input().split())
    if a>c:
        a,c = c,a
    if (b-a)==(c-b):
        print "0"
        continue
    ans = 0
    if b>c:
        ans += (b-c)
        b = c
    if b<a:
        ans += (a-b)
        b = a
    if (c+a)%2==1:
        if (b-a)>(c-b):
            c += 1
            ans += 1
        else:
            a -= 1
            ans += 1
    ans += abs((c+a)/2 - b)
    print ans
