# cook your code here
for t in range(input()):
    n = input()
    if n==1:
        print "XD"
        continue
    if n==2:
        print "XDD"
        continue
    if n==3:
        print "XDDD"
        continue
    if (n**0.5)==int(n**0.5):
        print "X"*int(n**0.5) + "D"*int(n**0.5)
        continue
    nd = int(n**0.5)+1
    nx = int(n/nd)
    nxb = n - nd*nx
    if nxb>0:
        s = "X"*nx + "D"*(nd-nxb) + "X" + "D"*(nxb)
    elif nxb==0:
        s = "X"*nx + "D"*(nd)
    print s
