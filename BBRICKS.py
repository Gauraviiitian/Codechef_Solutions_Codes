for t in range(int(input())):
    n, k = map(int, input().split())
    if k>n:
        print("0")
        continue
    x = 1
    count = 2*(n-k+1)
    f = min(k-1, n-k)
    c = 4
    n1 = ((n-k+1)*(n-k))//2
    n2 = k-1
    d2 = 1
    while f>0:
        a = c*n1*n2
        count += a
        n1 = ((n-k-x)*n1)//(x+2)
        n2 = (n2*(k-x-1))//(x+1)
        c = c*2
        x += 1
        f -= 1
    print(count%1000000007)