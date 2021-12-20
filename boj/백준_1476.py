E, S, M = map(int, input().split())
E1 = 0
S1 = 0
M1 = 0
year = 0

while True:
  year += 1
  E1 += 1
  S1 += 1
  M1 += 1
  if E1 > 15:
    E1 = 1
  if S1 > 28:
    S1 = 1
  if M1 > 19:
    M1 = 1 

  if E == E1 and S == S1 and M == M1:
    print(year)
    break

# https://www.acmicpc.net/problem/1476
