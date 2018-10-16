import math

def primeFactors(n):
    d = {2:0}
    while n%2==0:
            d[2] += 1
            n = n / 2
    for i in range(3, int(math.sqrt(n))+2, 2):
        d[i] = 0
        while n % i== 0:
            d[i] += 1
            n = n / i
    if n > 2 and !d.has_key(n):
        d[n] = 1
    return d
    
def addedFactors(d1, d2, n):
    d = {}
    rem1 = rem2 = 1
    for i in d1.keys():
        d[i] = min(d1[i], d2[i])*n
        if d1[i]>d2[i]:
            rem1 *= (i**(d1[i]-d2[i]))
        elif d1[i]<d2[i]:
            rem2 *= (i**(d2[i]-d1[i]))
    rem = primeFactors(rem1**n + rem2**n)
    for (i,j) in rem.items():
        if d.has_key(i):
            d[i] += j
        else:
            d[i] = j
    return d

def commonFactors(d1, d2):
    d = {}
    for (i,j) in d1.items():
        if d2.has_key(i):
            d[i] = min(j, d2[i])
    return d

print primeFactors(10)
for t in range(input()):
    a, b, n = map(int, raw_input().split())
    if a<b:
        a,b = b,a
    fact_a = primeFactors(a)
    fact_b = primeFactors(b)
    l = fact_b.keys()[-1]
    for i in fact_a.keys():
        if i>l:
            fact_b[i] = 0
            
    print fact_a
    print fact_b
    
    add_fact = addedFactors(fact_a, fact_b, n)
    print add_fact
    diff_fact = primeFactors(abs(a-b))
    #calculate independent factors of a^n+b^n
    print diff_fact
    ans = {}
    if a!=b:
        ans = commonFactors(add_fact, diff_fact)
    else:
        ans = fact_a
        ans[2] += 1
    if sum(ans.values())==0:
        print "1"
        continue
    res = 0
    print ans
    for (i, j) in ans.items():
        if j==0:
            continue
        res += (i**j)
        res = res%1000000007
    print res
#print mod(5, 8, 5)
