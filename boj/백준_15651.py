N, M = list(map(int, input().split()))

li = []

def DFS():
  if len(li) == M:
    print(' '.join(map(str, li)))
    return

  for i in range(1, N+1):
    li.append(i)
    DFS()
    li.pop()

DFS()

# https://www.acmicpc.net/problem/15651
