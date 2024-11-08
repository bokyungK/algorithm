N, M = map(int, input().split())

min_package_price = float("inf") 
min_each_price = float("inf") 

for _ in range(M):
  package_price, each_price = map(int, input().split())
  min_package_price = min(min_package_price, package_price)
  min_each_price = min(min_each_price, each_price)

only_package = (N // 6 + 1) * min_package_price
mix_pack_each = (N // 6) * min_package_price + (N % 6) * min_each_price
only_each = N * min_each_price

print(min(only_package, mix_pack_each, only_each))

