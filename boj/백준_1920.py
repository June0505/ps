import sys

def binary_search(a, b):
  start = 0
  end = len(a) - 1

  while start <= end:
    middle = (start + end) // 2
    if b == a[middle]:
      return 1
    elif b > a[middle]:
      start = middle + 1
    else:
      end = middle - 1
  return 0

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.sort()

m = int(input())
b = list(map(int, input().split()))

for i in range(m):
  print(binary_search(a, b[i]))

# https://www.acmicpc.net/problem/1920
