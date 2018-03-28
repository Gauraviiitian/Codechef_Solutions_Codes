for t in range(int(input())):
	n = int(input())
	li = []
	f=0
	for i in range(n):
		l = list(map(int, input().split()))
		l.sort()
		li.append(l)
	s = li[n-1][n-1]
	k = n-1
	for i in range(n-2, -1, -1):
	    j=n-1
	    f1=0
	    while li[i+1][k]<=li[i][j]:
	        if j == 0:
	            f1=1
	            break
	        j -= 1
	    if f1 == 1:
	        f=1
	        break
	    else:
	        s += li[i][j]
	        k = j
	if f == 1:
	    print("-1")
	else:
	    print(s)