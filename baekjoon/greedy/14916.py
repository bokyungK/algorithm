# 거스름돈

n = int(input())
coin_cnt = -1
share = n // 5;

while share > -1:
  if (n - share * 5) % 2 == 0:
    coin_cnt = share + (n - share * 5) // 2
    break
  else:
    share -= 1

print(coin_cnt)

# 거스름돈 개수를 최소화하기 위해 5로만 나눈 경우, 5와 2로 나눈 경우, 2로만 나눈 경우 순회