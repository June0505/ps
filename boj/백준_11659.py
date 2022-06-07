import sys

input = sys.stdin.readline

N, M = map(int, input().split())
number = list(map(int, input().split()))
prefix_sum = [0]

temp = 0
for i in number:
    temp += i
    prefix_sum.append(temp)
    
for i in range(M):
    a, b = map(int, input().split())
    print(prefix_sum[b] - prefix_sum[a-1])


# https://www.acmicpc.net/problem/11659
