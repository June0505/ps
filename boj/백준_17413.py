import sys

s = list(map(str, sys.stdin.readline().strip()))

res = ""
word = ""
reverse = True

for i in s:
    if i == '<':
        reverse = False
        res += word
        word = i

    elif i == '>':
        reverse = True
        res += (word + '>')
        word = ""

    elif i == ' ':
        res += word + i
        word = ""

    elif reverse:
        word = i + word

    else:
        word += i

print(res + word)

# https://www.acmicpc.net/problem/17413
