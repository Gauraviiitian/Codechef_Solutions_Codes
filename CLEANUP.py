for t in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    a1 = []
    a2 = []
    f = 1
    j = 0
    for i in range(1, n+1):
        if j>=m or arr[j]!=i:
            if f==1:
                f = 2
                a1.append(i)
            else:
                f = 1
                a2.append(i)
        else:
            j += 1
    for i in a1:
        print(i, end = " ")
    print()
    for i in a2:
        print(i, end = " ")
    print()