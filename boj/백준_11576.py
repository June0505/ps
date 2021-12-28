A, B = map(int, input().split())
M = int(input())
N = list(map(int, input().split()))[::-1]

num = 0 
result = []

for i in range(len(N)):
  num += N[i] * (A ** i)

while num != 0:
  result.append(num % B)
  num //= B

print(' '.join(map(str, result[::-1])))

# https://www.acmicpc.net/problem/11576
