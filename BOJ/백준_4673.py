def self_num(N):
    number = [int(i) for i in str(N)]
    N = N + sum(number)
    list2.append(N)

list1 = []
list2 = []

for i in range(1, 10000):
  list1.append(i)

for i in range(1, 10000):
  self_num(i)

complement = list(set(list1) - set(list2))
complement.sort()
complement.reverse()

for i in range(len(complement)):
  print(complement.pop())
