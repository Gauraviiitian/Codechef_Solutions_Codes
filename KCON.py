def maxSubArraySum(a,size):
     
    max_so_far =a[0]
    curr_max = a[0]
     
    for i in range(1,size):
        curr_max = max(a[i], curr_max + a[i])
        max_so_far = max(max_so_far,curr_max)
         
    return max_so_far


for t in range(int(input())):
    n, k = map(int, input().split())
    li = list(map(int, input().split()))
    tsum = sum(li)
    fsum = li[0]
    bsum = li[n-1]
    s = li[0]
    for i in range(1, n):
        s += li[i]
        if fsum<s:
            fsum = s
    s = li[n-1]
    for i in range(n-2, -1, -1):
        s += li[i]
        if bsum<s:
            bsum = s
    esum = fsum + bsum
    if tsum>0 and k>2:
        esum += tsum*(k-2)
    if k>1:
        li = li*2
        n = n*2
    msum = maxSubArraySum(li, n)
    if k==1:
        print(msum)
    else:
        print(max(esum, msum))
