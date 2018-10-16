""" Calculate till n==9 and then observe the pattern, and write values manually, that's it ;-)
z = int(input())
check = {}
arr = [i for i in range(1, z+1)]
for a in range(z):
    arr[0], arr[a] = arr[a], arr[0]
    for b in range(z):
        arr[1], arr[b] = arr[b], arr[1]
        for c in range(z):
            arr[2], arr[c] = arr[c], arr[2]
            for d in range(z):
                arr[3], arr[d] = arr[d], arr[3]
                for e in range(z):
                    arr[4], arr[e] = arr[e], arr[4]
                    for f in range(z):
                        arr[5], arr[f] = arr[f], arr[5]
                        for g in range(z):
                            arr[6], arr[g] = arr[g], arr[6]
                            for h in range(z):
                                arr[7], arr[h] = arr[h], arr[7]
                                for i in range(z):
                                    arr[8], arr[i] = arr[i], arr[8]
                                    if tuple(arr) not in check.keys():
                                        check[tuple(arr)] = 1
                                    else:
                                        check[tuple(arr)] += 1
                                    arr[8], arr[i] = arr[i], arr[8]
                                arr[7], arr[h] = arr[h], arr[7]
                            arr[6], arr[g] = arr[g], arr[6]
                        arr[5], arr[f] = arr[f], arr[5]
                    arr[4], arr[e] = arr[e], arr[4]
                arr[3], arr[d] = arr[d], arr[3]
            arr[2], arr[c] = arr[c], arr[2]
        arr[1], arr[b] = arr[b], arr[1]
    arr[0], arr[a] = arr[a], arr[0]

minval = 1000000007
maxval = 0
minp = []
maxp = []
for i in check.keys():
    if check[i]<=minval:
        minval = check[i]
        minp = i
    if check[i]>=maxval:
        maxval = check[i]
        maxp = i
#print(check)
print(maxp, minp)
"""
n = int(input())
if n==1:
    print("1\n1")
elif n==2:
    print("1 2\n2 1")
elif n==3:
    print("2 1 3\n3 1 2")
elif n==4:
    print("2 1 4 3\n4 2 3 1")
elif n==5:
    print("2 1 4 5 3\n5 1 2 3 4")
elif n==6:
    print("2 3 1 5 6 4\n6 1 2 3 4 5")
elif n==7:
    print("2 3 4 1 6 7 5\n7 1 2 3 4 5 6")
elif n==8:
    print("2 3 4 1 6 7 8 5\n8 1 2 3 4 5 6 7")
elif n==9:
    print("2 3 4 5 1 7 8 9 6\n9 1 2 3 4 5 6 7 8")
elif n==10:
    print("2 3 4 5 1 7 8 9 10 6\n10 1 2 3 4 5 6 7 8 9")
elif n==11:
    print("2 3 4 5 6 1 8 9 10 11 7\n11 1 2 3 4 5 6 7 8 9 10")
elif n==12:
    print("2 3 4 5 6 1 8 9 10 11 12 7\n12 1 2 3 4 5 6 7 8 9 10 11")
elif n==13:
    print("2 3 4 5 6 7 1 9 10 11 12 13 8\n13 1 2 3 4 5 6 7 8 9 10 11 12")
elif n==14:
    print("2 3 4 5 6 7 1 9 10 11 12 13 14 8\n14 1 2 3 4 5 6 7 8 9 10 11 12 13")
elif n==15:
    print("2 3 4 5 6 7 8 1 10 11 12 13 14 15 9\n15 1 2 3 4 5 6 7 8 9 10 11 12 13 14")
elif n==16:
    print("2 3 4 5 6 7 8 1 10 11 12 13 14 15 16 9\n16 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15")
elif n==17:
    print("2 3 4 5 6 7 8 9 1 11 12 13 14 15 16 17 10\n17 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16")
    