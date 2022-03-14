import sys
input = sys.stdin.readline

N = int(input())
Member = []
for i in range(N):
  age, name = input().split()
  age = int(age)
  Member.append((age, name))

Member.sort(key=lambda x : x[0])

for i in Member:
  print(i[0], i[1])

# https://www.acmicpc.net/problem/10814
