N = int(input())

for i in range(N):
  stack = []
  L = list(input().split())
  for _ in range(len(L)):
    stack.append(L.pop())
  answer = ' '.join(stack) 

  print("Case #{0}: {1}".format(i+1, answer))

# https://www.acmicpc.net/problem/12605
