import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())

martix = []
for i in range(N):
    martix.append(list(map(int, input().split())))

for _ in range(R):
    for i in range(min(N, M) // 2):
        x, y = i, i
        tmp = martix[x][y]
        
        for j in range(i + 1, N - i):  #좌
            x = j
            prev_value = martix[x][y]
            martix[x][y] = tmp
            tmp = prev_value
        
        for j in range(i + 1, M - i):  #하 
            y = j 
            prev_value = martix[x][y] 
            martix[x][y] = tmp  
            tmp = prev_value 

        for j in range(i + 1, N - i):  #우
            x = N - j - 1
            prev_value = martix[x][y]
            martix[x][y] = tmp
            tmp = prev_value
            
        for j in range(i + 1, M - i):  #상
            y = M - j -1
            prev_value = martix[x][y]
            martix[x][y] = tmp
            tmp = prev_value
            
for i in range(N):
    for j in range(M):
        print(martix[i][j], end=' ')
    print()
    
# https://www.acmicpc.net/problem/16926
