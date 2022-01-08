import sys
input = sys.stdin.readline

N = list(map(int, input().split()))

while True:
  if N[0] > N[1]:
    one = N[0] 
    two = N[1] 
    N[0] = two
    N[1] = one
    if N != [1, 2, 3, 4, 5]:
      tmp = list(map(str, N))
      print(' '.join(tmp))  

  if N[1] > N[2]:
    two = N[1] 
    three = N[2] 
    N[1] = three
    N[2] = two
    if N != [1, 2, 3, 4, 5]:
      tmp = list(map(str, N))
      print(' '.join(tmp))  

  if N[2] > N[3]:
    three = N[2] 
    four = N[3] 
    N[2] = four
    N[3] = three
    if N != [1, 2, 3, 4, 5]:
      tmp = list(map(str, N))
      print(' '.join(tmp))  

  if N[3] > N[4]:
    four = N[3] 
    five = N[4] 
    N[3] = five
    N[4] = four
    if N != [1, 2, 3, 4, 5]:
      tmp = list(map(str, N))
      print(' '.join(tmp))  

  if N == [1, 2, 3, 4, 5]:
    tmp = list(map(str, N))
    print(' '.join(tmp))  
    break

# https://www.acmicpc.net/problem/2947
