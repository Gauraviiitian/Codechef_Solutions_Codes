# cook your code here
for t in range(input()):
    n, m = map(int, raw_input().split())
    matrix = []
    for i in range(n):
        mt = map(int, raw_input().split())
        matrix.append(mt)
            
    f = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j]==-1:
                if i==0 and j==0:
                    matrix[i][j] = 1
                    continue
                
                if i>0 and j<m-1 and matrix[i-1][j]>matrix[i][j+1] and matrix[i][j+1]!=-1:
                    f = 1
                    break
                if i<n-1 and j>0 and matrix[i][j-1]>matrix[i+1][j] and matrix[i+1][j]!=-1:
                    f = 1
                    break
                
                if i==0 and j>0:
                    matrix[i][j] = matrix[i][j-1]
                if j==0 and i>0:
                    matrix[i][j] = matrix[i-1][j]
                if i>0 and j>0:
                    matrix[i][j] = max(matrix[i-1][j],matrix[i][j-1])
                    
            else:
                if i>0 and matrix[i][j]<matrix[i-1][j]:
                    f = 1
                    break
                if j>0 and matrix[i][j]<matrix[i][j-1]:
                    f = 1
                    break
                    
        if f==1:
            break
        
    if f==0:
        for i in range(n):
            for j in range(m):
                print matrix[i][j], 
            print 
    else:
        print "-1"
                
