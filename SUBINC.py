for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    l = 1
    i = 0
    for i in range(n-1):
        if a[i]<=a[i+1]:
            l += 1
        else:
            l = 1
        count += l
    print(count)