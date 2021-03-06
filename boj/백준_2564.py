import sys
input = sys.stdin.readline

def get_distance(x, y): 
    if x == 1:  # λΆ
        return y
    if x == 2:  # λ¨
        return w + h + w - y
    if x == 3:  # μ
        return w + h + w + h - y
    if x == 4:  # λ
        return w + y

w, h = map(int, input().split())
n = int(input())

course = [] 
for _ in range(n + 1):
    x, y = map(int, input().split())
    course.append(get_distance(x, y))

answer = 0

for i in range(n): 
    in_course = abs(course[-1] - course[i])
    out_course = 2 * (w + h) - in_course
    answer += min(in_course, out_course)

print(answer)

# https://www.acmicpc.net/problem/2564
