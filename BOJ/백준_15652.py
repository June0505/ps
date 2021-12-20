N, M = list(map(int, input().split()))

li = []

def DFS(start):
  if len(li) == M:
    print(' '.join(map(str, li)))
    return

  for i in range(start, N+1):
    li.append(i)
    DFS(i)
    li.pop()

DFS(1)

# https://www.acmicpc.net/problem/15652
