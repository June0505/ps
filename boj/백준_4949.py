while True:
    s = input()
    if s == '.':
        break
    stack = []
    flag = True
    
    for i in s:
        if i == '(' or i == '[':
            stack.append(i) #PUSH
            
        elif i == ')':
            if not stack or stack[-1] == '[': #불균형
                flag = False
                break
            elif stack[-1] == '(':
                stack.pop() #POP
                
        elif i == ']': 
            if not stack or stack[-1] == '(': #불균형
                flag = False
                break
            elif stack[-1] == '[':
                stack.pop() #POP
         
    if flag and not stack:
        print('yes')
    else:
        print('no')

# https://www.acmicpc.net/problem/4949
