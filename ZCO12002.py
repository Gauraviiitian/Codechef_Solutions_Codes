# cook your code here
n, x, y = map(int, raw_input().split())
cont = []
for i in range(n):
    cont.append(map(int, raw_input().split()))
v = map(int, raw_input().split())
w = map(int, raw_input().split())
v.sort()
w.sort()
min_t = 1000000001
for c in cont:
    if c[0]<v[0] or c[1]>w[y-1]:
        continue
    
    low = 0
    high = x-1
    mid = 0
    while low<=high:
        mid = (low+high)/2
        if c[0]==v[mid]:
            break
        elif c[0]<v[mid]:
            high = mid-1
        else:
            low = mid+1
    if c[0]>=v[mid]:
        t1 = v[mid]
    else:
        t1 = v[mid-1]
        
    low = 0
    high = y-1
    mid = 0
    while low<=high:
        mid = (low+high)/2
        if c[1]==w[mid]:
            break
        elif c[1]<w[mid]:
            high = mid-1
        else:
            low = mid+1
    if c[1]<=w[mid]:
        t2 = w[mid]
    else:
        t2 = w[mid+1]
    new_t = t2-t1+1
    if new_t<min_t:
        min_t = new_t

print min_t
