# 주유소
N = int(input())
roads = list(map(int, input().split()))
prices = list(map(int, input().split()))

liter = 0
minPrice = prices[0]

for i in range(N - 1):
  if prices[i] < minPrice:
    minPrice = prices[i]

  liter += roads[i] * minPrice

print(liter)