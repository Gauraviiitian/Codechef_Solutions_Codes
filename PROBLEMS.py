p, s = map(int, raw_input().split())
level = []
for j in range(p):
    a = []
    b = map(int, raw_input().split())
    c = map(int, raw_input().split())
    for i in range(s):
        a.append([b[i], c[i]])
    a.sort()
    count = 0
    for i in range(s-1):
        if a[i][1]>a[i+1][1]:
            count += 1
    level.append([count, j+1])
level.sort()
for l in level:
    print l[1]
