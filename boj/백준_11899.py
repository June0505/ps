answer = 0

s = input()
stack = []

for i in range(len(s)):  
  if not stack and s[i] == ')':
    answer += 1
    
  elif s[i] == '(':
    stack.append('(')
  
  elif stack and s[i] == ')':
    stack.pop()

print(answer + len(stack))

# https://www.acmicpc.net/problem/11899
