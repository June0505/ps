import string

A, B = map(int, input().split())
tmp = string.digits+string.ascii_uppercase

def convert(number, base):
  q, r = divmod(number, base)
  if q == 0:
    return tmp[r]
  else:
    return convert(q, base) + tmp[r]

print(convert(A, B))

# https://www.acmicpc.net/problem/11005
