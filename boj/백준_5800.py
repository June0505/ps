import sys
input = sys.stdin.readline

S = []
Max = []
Min = []
N = int(input())

for i in range(N):
  li = list(map(int, input().split()))
  del li[0]
  li.sort()
  S.append(li)
  Max.append(max(li))
  Min.append(min(li))

L_gap = []
for i in S:
  tmp = []
  for j in range(len(i)-1):
    gap = abs(i[j] - i[j+1])
    tmp.append(gap)
  L_gap.append(max(tmp))

for i in range(N):
  print('Class {0}'.format(i+1))
  print('Max {0}, Min {1}, Largest gap {2}'.format(Max[i], Min[i], L_gap[i]))

# https://www.acmicpc.net/problem/5800
