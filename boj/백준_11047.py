import sys

input = sys.stdin.readline
N, K = map(int, input().split())
coin_li = []
cnt = 0

for _ in range(N):
  coin_li.append(int(input()))

coin_li = (list(reversed(coin_li)))

for i in coin_li:
  if i <= K:
    cnt += (K // i)
    K %= i

print(cnt)

# https://www.acmicpc.net/problem/11047
