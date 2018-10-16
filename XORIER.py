for t in range(int(input())):
    n = int(input())
    arr = map(int, input().split())
    eva = []
    oda = []
    for i in arr:
        if i%2==0:
            eva.append(i)
        else:
            oda.append(i)
    #print(eva, oda)
    e = len(eva)
    o = n-e
    freqe = [0]*250001 #frequency of each number
    freqo = [0]*250001 #frequency of each number
    count = (e*(e-1)//2) + (o*(o-1))//2
    
    for i in range(e):
        eva[i] = eva[i]>>2
        freqe[eva[i]] += 1
    
    for i in range(o):
        oda[i] = oda[i]>>2
        freqo[oda[i]] += 1
    #print(freqe[:5], freqo[:5])
    for i in range(250001):
        if freqe[i]>1:
            count -= (freqe[i]*(freqe[i]-1))//2
        if freqo[i]>1:
            count -= (freqo[i]*(freqo[i]-1))//2
    
    print(count)