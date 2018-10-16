# cook your code here
# find frequecy of max elements using which we can/
# the required subarray sum
for t in range(input()):
    n, k = map(int, raw_input().split())
    arr = map(int, raw_input().split())
    s = list(set(arr))
    freq = {}
    for i in s:
        freq[i]=0
    s.sort(reverse=True)
    for i in range(n):
        freq[arr[i]] += 1
    
    #print freq
    ans = [0]*(k+1)
    
    for i in s:
        if freq[i]%2==1:
            ans[1] = i
            break
        
    for i in range(2, k+1):
        j = i
        x = 0
        #print "yes"
        while j>0:
            if j==1:
                ans[i] += s[x]
                break
            if j<freq[s[x]]:
                if x==0 and (j%2==0 and freq[s[x]]%2==1) and (j%2==1 and freq[s[x]]%2==0):
                    ans[i] += (j-1)*s[x]
                    x += 1
                    j = 1
                else:
                    ans[i] += s[x]*j
                    j = 0
            else:
                ans[i] += s[x]*freq[s[x]]
                j -= freq[s[x]]
                x += 1
    for i in range(1, k+1):
        print ans[i],
    print 
