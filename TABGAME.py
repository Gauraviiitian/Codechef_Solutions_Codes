# cook your dish here
for t in range(int(input())):
    a = input()
    b = input()
    m = len(a)
    n = len(b)
    board = ["" for i in range(n+1)]
    board[0] = '1' + a
    for i in range(1, n+1):
        board[i] = b[i-1]
    for j in range(1,m+1):
        board[1] += str(1 - (int(board[0][j]) & int(board[1][j-1])))
        if n>1:
            board[2] += str(1 - (int(board[1][j]) & int(board[2][j-1])))
    for i in range(3, n+1):
        board[i] = b[i-1]+str(1-(int(board[i][0]) & int(board[i-1][1])))
        if m>1:
            board[i] += str(1-(int(board[i][1]) & int(board[i-1][2])))
    q = int(input())
    for Q in range(q):
        x, y = map(int, input().split())
        if x>2 and y>2:
            if x<y:
                print(board[2][y-(x-2)], end = "")
            else:
                print(board[x-(y-2)][2], end = "")
        else:
            print(board[x][y], end = "")
    print()