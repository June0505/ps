import string

N, B = input().split(' ')

N = ''.join(reversed(N))
B = int(B)
tmp = string.digits+string.ascii_uppercase
result = 0

for x in range(len(N)-1, -1, -1):
  summary = tmp.index(N[x]) * (B**x)
  result += summary

print(result)

# https://www.acmicpc.net/problem/2745
