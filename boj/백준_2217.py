import sys
input = sys.stdin.readline

N = int(input())
li = []
value = []

for _ in range(N):
  rope = int(input())
  li.append(rope)

li.sort(reverse=True)

for num in range(N):
  value.append(li[num] * (num+1))

print(max(value))

# https://www.acmicpc.net/problem/2217
