import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def dfs(y, x):
    dx = [1, 1, 1, 0, 0, -1, -1, -1]
    dy = [-1, 0, 1, 1, -1, 0, -1, 1]
    graph[y][x] = 0 
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < N) and (0 <= ny < M):
            if graph[ny][nx] == 1:
                graph[ny][nx] = 0
                dfs(ny, nx)

M, N = map(int, input().split())
graph = []
for i in range(M):
    graph.append(list(map(int, input().split())))

answer = 0
for i in range(M):
    for j in range(N):
        if graph[i][j]:
            dfs(i, j)
            answer += 1

print(answer)

# https://www.acmicpc.net/problem/14716
