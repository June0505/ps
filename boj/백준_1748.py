N = int(input())
length_N = len(str(N))
count = 0

for i in range(length_N-1) :
    count += 9 * 10 ** i * (i + 1)

print(count + (N - 10 ** (length_N-1) + 1) * length_N)

# https://www.acmicpc.net/problem/1748
