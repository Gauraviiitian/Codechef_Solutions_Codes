# cook your code here
n = input()
sumn = {}
for i in range(n):
    sumn[i] = 0
x = []
for i in range(n):
    a,b,c = map(int, raw_input().split())
    x.append([a, b+c])
x = sorted(x, key = lambda t: t[1], reverse = True)
acc_s = 0
max_count = 0
for i in x:
    sumi = acc_s + i[0] + i[1]
    acc_s += i[0]
    if sumi>max_count:
        max_count = sumi
print max_count
