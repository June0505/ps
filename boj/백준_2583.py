import sys

sys.setrecursionlimit(10000)  # 재귀 최대 깊이 설정

def dfs(x, y):
    global cnt
    graph[x][y] = 1
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if graph[nx][ny] == 0:
                cnt += 1
                dfs(nx, ny)

M, N, K = map(int, input().split())

graph = [[0] * N for i in range(M)]

cnt = 1  # 영역 넓이
answer = []  # 영역 넓이 리스트
area = 0  # 영역 갯수

for _ in range(K):
    lx, ly, rx, ry = map(int, input().split())
    for i in range(ly, ry):
        for j in range(lx, rx):
            graph[i][j] = 1

for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            area += 1
            dfs(i, j)
            answer.append(cnt)
            cnt = 1  # 초기화

answer.sort()
print(area)
print(' '.join(map(str, answer)))

# https://www.acmicpc.net/problem/2583
