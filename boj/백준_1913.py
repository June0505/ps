N = int(input())
M = int(input())
board = [[0] * N for i in range(N)]
count = []
tmp = 1
check = 1
number = 1
cnt = 0

for _ in range((N-1) * 2):
  count.append(tmp)
  cnt += 1
  if cnt == 2:
    tmp += 1
    cnt = 0

# 시작 부분
count.append(N-1)
start = N // 2
board[start][start] = 1
row = start
column = start

# 상: 1, 우: 2, 하: 3, 좌: 4
for i in count:
  for _ in range(i):
    number += 1
    if check == 1:
      row -= 1
      board[row][column] = number

    elif check == 2:
      column += 1
      board[row][column] = number

    elif check == 3:
      row += 1
      board[row][column] = number
    
    elif check == 4:
      column -= 1
      board[row][column] = number
    
  check += 1
  if check == 5:
    check = 1

# 출력
for i in range(N): 
  for j in range(N): 
    print(board[i][j], end=" ") 
    if (board[i][j] == M):
       save_x = i+1 
       save_y = j+1 
  print() 

print(save_x, save_y)

# https://www.acmicpc.net/problem/1913
