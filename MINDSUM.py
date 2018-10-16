ds = [i for i in range(10)]
for i in range(10, 2000007):
    s = ds[i//10] + ds[i%10]
    ds.append(s)

def findmin(n, d, c):
    if c==11 or n==1:
        return n*100+c
    if n<10:
        return min(n*100 + c, findmin(n+d, d, c+1))
    else:
        n1 = ds[n//100000] + ds[n%100000]
        #m = min([n, c], findmin(n1, d, c+1), findmin(n+d, d, c+1))
        #print(m)
        return min(n*100 + c, findmin(n1, d, c+1), findmin(n+d, d, c+1))

for t in range(int(input())):
    n, d = map(int, input().split())
    if n==1:
        print("1 0")
        continue
    ans = findmin(n, d, 0)
    print(ans//100, ans%100)