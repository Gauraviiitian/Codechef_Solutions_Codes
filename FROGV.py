n, k, p = map(int, input().split())
a = list(map(int, input().split()))

l = [0]*(n)
m = [0]*(n+1)
d = [[0, 0] for i in range(n)]
for i in range(n):
    d[i][0] = a[i]
    d[i][1] = i+1
d.sort(key = lambda x: x[0])

count = 1
l[0] = 1
last_found = 0
for i in range(1, n):
    if (d[i][0] - d[last_found][0])>k:
        l[i] = count+1
        count += 1
    else:
        l[i] = count
    last_found = i
    
for i in range(n):
    m[d[i][1]] = i
#print(d)
#print(l)

for i in range(p):
    x, y = map(int, input().split())
    if l[m[x]]==l[m[y]]:
        print("Yes")
    else:
        print("No")