# 보물
length = int(input())
minSum = 0

a = list(map(int, input().split(' ')))
b = list(map(int, input().split(' ')))

a.sort(reverse=True)
b.sort()

for i in range(length):
  minSum += a[i] * b[i]

print(minSum)