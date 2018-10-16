# cook your dish here
import math
for t in range(int(input())):
    n, a = map(int, input().split())
    ss = ""
    min_len = 1
    if a==1:
        print(n, "a"*n)
        continue
    for i in range(a):
        ss += chr(97+i)
    if n<=a:
        print(min_len, ss[:n])
        continue
    if a>2:
        print(min_len, (ss*(n//a + 1))[:n])
        continue
    if n==2:
        print("1 ab")
    elif n==3:
        print("2 aab")
    elif n==4:
        print("2 aabb")
    elif n==5:
        print("3 aabbb")
    elif n==6:
        print("3 aaabbb")
    elif n==7:
        print("3 aaababb")
    elif n==8:
        print("3 aaababbb")
    elif n==9:
        print("4 aaababbbb")
    else:
        s = "babaabbabaab"*(n//12 + 1)
        print(4, s[:n])
