# cook your code here
n1, n2, n3 = map(int, raw_input().split())
l1 = []
l2 = []
l3 = []
ans = []
for i in range(n1):
    l1.append(input())
for i in range(n2):
    l2.append(input())
for i in range(n3):
    l3.append(input())
i=j=k=0
while i<n1 or j<n2 or k<n3:
    if i<n1:
        c1 = l1[i]
    else:
        c1 = 1000000001
    if j<n2:
        c2 = l2[j]
    else:
        c2 = 1000000002
    if k<n3:
        c3 = l3[k]
    else:
        c3 = 1000000003
    m = min(c1,c2,c3)
    count = 0
    if m==c1:
        count += 1
        i += 1
    if m==c2:
        count += 1
        j += 1
    if m==c3:
        count += 1
        k += 1
    if count>=2:
        ans.append(m)
print len(ans)
for i in ans:
    print i
