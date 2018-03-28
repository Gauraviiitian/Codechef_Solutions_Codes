t = int(input())
for t in range(t):
        a, b, c, d = map(int, input().split())
        f=0
        if a==b and b==c:
                f=1
        if a==c and b==d:
                f=1
        if a==d and b==c:
                f=1
        if f==1:
                print("YES")
        else:
                print("NO")
