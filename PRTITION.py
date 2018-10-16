# cook your dish here
for t in range(int(input())):
    x,n = map(int, input().split())
    s = (n*(n+1))//2 - x
    if n==2 or s%2==1:
        print("impossible")
        continue
    arr = ['0']*(n+1);
    arr[x] = '2'
    ss = s//2
    for i in range(n, 0, -1):
        if i!=x and ss>=i and ss-i!=x:
            ss -= i
            arr[i]='1'
        if ss==0:
            break
    if ss!=0:
        print("impossible")
    else:
        print("".join(arr[1:]))
