# 2 = 청소, 1 = 벽
# d = 0-북, 1-동, 2-남, 3-서

N, M = map(int, input().split())
r, c, d = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

def left():
    global d
    d = (d - 1) % 4

cnt = 1
x, y = r, c
arr[x][y] = 2  # 방문처리

while True:
    check = False
    for i in range(4):
        left()
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < N and 0 <= ny < M:  # 그래프 안
            if arr[nx][ny] == 0:
                cnt += 1
                arr[nx][ny] = 2
                x, y = nx, ny
                check = True
                break

    if not check:
        nx = x - dx[d]
        ny = y - dy[d]
        if 0 <= nx < N and 0 <= ny < M:
            if arr[nx][ny] == 2:
                x, y = nx, ny
            elif arr[nx][ny] == 1:
                print(cnt)
                break
        else:
            print(cnt)
            break

# https://www.acmicpc.net/problem/14503
