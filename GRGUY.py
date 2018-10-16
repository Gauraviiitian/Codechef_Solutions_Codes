# cook your dish here
for t in range(int(input())):
    a = input()
    b = input()
    n = len(a)
    if a[0]=='#' and b[0]=='#':
        print("No")
        continue
    
    f1 = 1
    c1 = 0
    j = 1
    if a[0]=='.':
        for i in range(1, n):
            if a[i]=='#' and b[i]=='#':
                f1 = 0
                break
            if j==1 and a[i]=='.':
                continue
            elif j==2 and b[i]=='.':
                continue
            else:
                if j==1:
                    j = 2
                else:
                    j = 1
                c1 += 1
    else:
        f1 = 0
                
    c2 = 0
    j = 2
    f2 = 1
    if b[0]=='.':
        for i in range(1, n):
            if a[i]=='#' and b[i]=='#':
                f2 = 0
                break
            if j==1 and a[i]=='.':
                continue
            elif j==2 and b[i]=='.':
                continue
            else:
                if j==1:
                    j = 2
                else:
                    j = 1
                c2 += 1
    else:
        f2 = 0
    
    if f1 and f2:
        print("Yes")
        print(min(c1, c2))
    elif f1==1:
        print("Yes")
        print(c1)
    elif f2==1:
        print("Yes")
        print(c2)
    else:
        print("No")