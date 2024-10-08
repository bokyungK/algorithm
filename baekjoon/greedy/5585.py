# 거스름돈
price = int(input())
totalChange = 1000 - price
changeList = [500, 100, 50, 10, 5, 1]
count = 0

for change in changeList:
  count += totalChange // change
  totalChange = totalChange % change
  
  if totalChange % change == 0:
    break

print(count)