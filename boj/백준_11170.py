T = int(input())

for _ in range(T):
  N, M = input().split()
  answer = 0
  for i in range(int(N), int(M)+1):
    answer += str(i).count('0')
  print(answer)

# https://www.acmicpc.net/problem/11170
