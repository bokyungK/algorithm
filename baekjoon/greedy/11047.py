# 동전 0

# 입력 받기
n, k = map(int, input().split())
coinList = []
count = 0

for _ in range(n):
    coinList.append(int(input()))

# 동전 개수
for coin in list(reversed(coinList)):
    if k // coin > 0:
        count += k // coin
        k %= coin

print(count)

# 메모 : (line 15) 비교에 기준이 되는 값은 연산이 끝나고 재할당!