for t in range(input()):
    n = input()
    arr = map(int, raw_input().split())
    a = [0]
    b = [0] 
    lena = 1
    for i in range(1, n):
        h = lena-1
        l = 0
        if arr[i]>arr[a[h]]:
            a.append(i)
            b.append(i)
            lena += 1
            continue
        while(h>l):
            mid = (l+h)/2
            if arr[i]==arr[a[mid]]:
                h = mid
                break
            elif arr[i]>arr[a[mid]]:
                l = mid+1
            else:
                h = mid
        
        b[h] = i
    #print a 
    #print b
    max_len = 0
    for i in range(lena):
        max_len = max(max_len, b[i]-a[i]+1)
    print max_len
