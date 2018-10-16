# cook your code here
for t in range(input()):
    s = raw_input()
    d = [0]*26
    for i in s:
        d[ord(i)-97] += 1
    d.sort()
    flag = 0
    if len(d)<3:
        print "Dynamic"
        continue
    for j in range(26):
        if d[j]!=0:
            break
    for i in range(2, 26-j):
        if d[i+j]==0 or d[i+j-1]==0 or d[i+j-2]==0:
            continue
        if i==3 and (d[j+3]==d[j+0]+d[j+2] or d[j+3]==d[j+1]+d[j+2]):
            continue
        if d[i+j] != (d[i+j-1] + d[i+j-2]):
            flag = 1
            break
    if flag==1:
        print "Not"
    else:
        print "Dynamic"
