# cook your code here
for t in range(input()):
    n = input()
    a = map(int, raw_input().split())
    b = map(int, raw_input().split())
    sum_a = sum(a)-max(a)
    sum_b = sum(b)-max(b)
    if sum_a<sum_b:
        print "Alice"
    elif sum_a>sum_b:
        print "Bob"
    else:
        print "Draw"
