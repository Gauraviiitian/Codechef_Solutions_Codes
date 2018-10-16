# cook your dish here
for t in range(int(input())):
    n, m, x, y = map(int, input().split())
    n -= 1
    m -= 1
    
    if(n==1 and m==1) or (n==0 and m==0):
        print("Chefirnemo")
    elif (n==0 and m==y) or (m==0 and n==x):
        print("Chefirnemo")
    elif (n%x==0 and m%y==0) or (n>0 and m>0 and (n-1)%x==0 and (m-1)%y==0):
        print("Chefirnemo")
    else:
        print("Pofik")