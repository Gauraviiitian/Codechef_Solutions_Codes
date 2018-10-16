# cook your dish here
n, q, l, r = map(int, input().split())
li = [0]*n
for Q in range(q):
    t, x, y = map(int, input().split())
    if q == 1:
        li.pop(x-1)
        li.insert(x-1, y)
    elif q == 2:
        x -= 1
        y -= 1
        len = y-x+1
        count = [0]*len
        sli = []
        for i in range(x, y+1):
            sli.append(li[x])
            if sli[i] in range(l, r+1):
                count[i-x] += 1
            else:
                continue
            for j in range(i+1, y+1):
                sli.append(li[y])
                max = max(sli)
                if max in range(l, r+1):
                    count[j-x] += 1
                else:
                    break
        sum = 0
        for i in count:
            sum += i
        print(sum)
        
