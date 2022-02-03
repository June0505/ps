from collections import deque

n, m = map(int, input().split())
li = list(map(int, input().split()))
q = deque([i for i in range(1, n+1)])

answer = 0
for i in range(m):

  #큐의 앞쪽
  if q.index(li[i]) < len(q) - q.index(li[i]): 
    while True:
      if q[0] == li[i]:
        q.popleft()
        break
      else:
        q.rotate(-1)
        answer += 1

  #큐의 뒤쪽    
  else:                                      
    while True:
      if q[0] == li[i]:
        q.popleft()
        break
      else:
        q.rotate()
        answer += 1

print(answer)

# https://www.acmicpc.net/problem/1021
