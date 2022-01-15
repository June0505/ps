import sys
input = sys.stdin.readline

S = list(input().rstrip())
T = list(input().rstrip())

for _ in range(len(T)-len(S)):
  if T[-1] == 'A':
    T.pop()
  
  elif T[-1] == 'B':
    T.pop()
    T.reverse()

if S == T:
  print(1)
else:
  print(0)

# https://www.acmicpc.net/problem/12904
