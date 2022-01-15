import sys
input = sys.stdin.readline

N = int(input())

arr = []
answer = [0 for _ in range(1000)]

for i in range(N):
  d, w = map(int, input().split())
  arr.append([d, w])

arr.sort(reverse=True, key=lambda x : x[1])

for i in range(N):
  for j in range(arr[i][0]-1, -1, -1):
    if answer[j] == 0:
      answer[j] = arr[i][1]
      break

print(sum(answer))

# https://www.acmicpc.net/problem/13904
