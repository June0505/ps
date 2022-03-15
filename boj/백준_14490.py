def gcd(a, b):
  while b > 0:
    a, b = b, a % b
  return a

n, m = input().split(":")
x = gcd(int(n), int(m))
n = int(n) // x
m = int(m) // x

print(str(n) + ':' + str(m))

# https://www.acmicpc.net/problem/14490
