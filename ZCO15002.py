# cook your code here
n, k = map(int, raw_input().split())
a = map(int, raw_input().split())
a.sort()
count = 0
i = 0
j = 1
while i<n and j<n:
    if a[j]-a[i]>=k:
        i += 1
        count += n-j
    else:
        j += 1
print count
