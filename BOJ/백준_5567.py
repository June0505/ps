import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

person = []
friend = []
friend_of_friend = []

for i in range(M):
  a, b = map(int, input().split())
  if a == 1:
    friend.append(b)
  else:
    tmp = [a, b]
    person.append(tmp)

for i in person:
  for j in friend:
    if j in i: 
      friend_of_friend.append(i[0])
      friend_of_friend.append(i[1])

result = friend + friend_of_friend
set_result = set(result)
result = list(set_result)

print(len(result))
