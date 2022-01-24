N = int(input())
d = {}
li = []

for _ in range(N):
  book = input()
  li.append(book)

for b in li:
  if b in d:
    d[b] += 1
  else:
    d[b] = 1

result = [k for k, v in d.items() if max(d.values()) == v]

result.sort()

print(result[0])

# https://www.acmicpc.net/problem/1302
