N, M = list(map(int, input().split()))

li = []

def dfs():
  if len(li) == M:
    print(' '.join(map(str, li)))
    return

  for i in range(1, N + 1):
    if not i in li:
      li.append(i)
      dfs()
      li.pop()

dfs()

# https://www.acmicpc.net/problem/15649
