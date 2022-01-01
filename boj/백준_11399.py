N = int(input())
P = list(map(int, input().split()))
t = 0
result = 0
P.sort()

for i in P:
  t += i
  result += t

print(result)

# https://www.acmicpc.net/problem/11399
