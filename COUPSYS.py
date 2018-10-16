# cook your code here
for t in range(input()):
    n = input()
    max_dis = [0]*4
    city = [101]*4
    for i in range(n):
        c, l, x = map(int, raw_input().split())
        if max_dis[l]<x:
            max_dis[l] = x
            city[l]=c
        elif max_dis[l]==x:
            if city[l]>c:
                city[l]=c
            
    print max_dis[1], city[1]
    print max_dis[2], city[2]
    print max_dis[3], city[3]
