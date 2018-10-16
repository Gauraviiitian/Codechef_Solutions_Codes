for t in range(input()):
    n, a, b = map(int, raw_input().split())
    count_a = count_b = 0.0
    d = map(int, raw_input().split())
    for i in d:
        if i==a:
            count_a += 1
        if i==b:
            count_b += 1
    ans = count_a*count_b/(n**2)
    print ans
