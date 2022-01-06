import sys
input = sys.stdin.readline

N = int(input())
li = list(map(int, input().split()))
answer = [0] * N

# 가장 작은 수 
answer[li[0]] = 1

num = 0

for i in range(1, len(li)-1):
  idx = -1
  cnt = -1
  num = i + 1 # 3
  for j in answer:
    idx += 1
    if j == 0:
      cnt += 1
    
    if cnt == li[i] and j == 0:
      answer[idx] = num

for i in range(len(answer)):
  if answer[i] == 0:
    answer[i] = N

result = []

for i in answer:
  result.append(str(i))

print(' '.join(result))

# https://www.acmicpc.net/problem/1138
