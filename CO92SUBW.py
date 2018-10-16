# cook your code here
import math
for t in range(input()):
    x = input()
    k = (int)(-1+(1.0+8.0*x)**0.5)/2
    dis1 = k + x - (k*(k+1)/2)
    dis2 = (k+1) + ((k+1)*(k+2)/2) - x
    print min(dis1, dis2)
            
