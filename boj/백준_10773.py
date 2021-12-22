import sys

K = int(sys.stdin.readline().rstrip())
li = []
answer = 0

for _ in range(K):
  Num = int(sys.stdin.readline().rstrip())
  if Num != 0:
    li.append(Num)
  else:
    li.pop()

for i in li:
  answer += i

print(answer)

# https://www.acmicpc.net/problem/10773
