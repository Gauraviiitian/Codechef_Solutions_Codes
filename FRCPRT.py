def left(a, b):
    n = len(a)
    m = len(a[0])
    for i in range(n):
        for j in range(m):
            if j<b[i]:
                a[i][j] = "1"
            else:
                a[i][j] = "0"

def right(a, b):
    n = len(a)
    m = len(a[0])
    for i in range(n):
        for j in range(m):
            if j<m-b[i]:
                a[i][j] = "0"
            else:
                a[i][j] = "1"

def up(a, b):
    n = len(a)
    m = len(a[0])
    for i in range(n):
        for j in range(m):
            if i<b[j]:
                a[i][j] = "1"
            else:
                a[i][j] = "0"

def down(a, b):
    n = len(a)
    m = len(a[0])
    for i in range(n):
        for j in range(m):
            if i<n-b[j]:
                a[i][j] = "0"
            else:
                a[i][j] = "1"

def disp(a):
    for i in a:
        print "".join(i)

for t in range(input()):
    n, m = map(int, raw_input().split())
    a = []
    for i in range(n):
        a.append(list(raw_input()))
    q = raw_input()
    row_sum = [0]*n
    col_sum = [0]*m
    for i in range(n):
        row_sum[i] = a[i].count("1")
    for i in range(n):
        for j in range(m):
            if a[i][j] == "1":
                col_sum[j] += 1
                
    if q[0]=="L":
        left(a, row_sum)
    elif q[0]=="R":
        right(a, row_sum)
    elif q[0]=="U":
        up(a, col_sum)
    elif q[0]=="D":
        down(a, col_sum)
    
    i = 0
    c1 = ""
    c2 = ""
    x = y = 0
    while i<len(q):
        if q[i]=="L" or q[i]=="R":
            c1 = q[i]
            x = i
        else:
            c2 = q[i]
            y = i
        i += 1
        
    for i in range(n):
        row_sum[i] = a[i].count("1")
    for i in range(m):
        col_sum[i] = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] == "1":
                col_sum[j] += 1
               
    if y>x:
        if c1=="L":
            left(a, row_sum)
        elif c1=="R":
            right(a, row_sum)
        for i in range(m):
            col_sum[i] = 0
        for i in range(n):
            for j in range(m):
                if a[i][j] == "1":
                    col_sum[j] += 1        
        if c2=="U":
            up(a, col_sum)
        elif c2=="D":
            down(a, col_sum)
    else:
        if c2=="U":
            up(a, col_sum)
        elif c2=="D":
            down(a, col_sum)
        for i in range(n):
            row_sum[i] = a[i].count("1")
        if c1=="L":
            left(a, row_sum)
        elif c1=="R":
            right(a, row_sum)
    disp(a)
