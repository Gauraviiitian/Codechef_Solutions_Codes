# cook your code here
n = input()
s = []
for i in range(n):
    s.append(raw_input())
q = input()
for i in range(q):
    r, p = raw_input().split()
    r = int(r)
    st = s[:r]
    st.sort()
    max_len = -1
    for i in range(r):
        j = 0
        while j<min(len(p), len(st[i])) and p[j]==st[i][j]:
            j += 1
        if j>max_len:
            max_len = j
            ans = st[i]
    print ans
