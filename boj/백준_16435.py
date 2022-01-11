import sys
input = sys.stdin.readline

N, L = map(int, input().split())
li = list(map(int, input().split()))

li.sort()

for h in li:
  if h <= L:
    L += 1
  else:
    break

print(L)

# https://www.acmicpc.net/problem/16435
