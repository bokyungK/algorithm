# 카드 정렬하기

# <첫 번째 시도 - 실패>

# N = int(input())
# cards = []
# total = 0
# current = 0

# for _ in range(N):
#   cards.append(int(input()))

# cards.sort()

# for card in cards:
#   current += total + card
#   total = card

# print(current)

# 메모 : 단순히 작은 수부터 순차적으로 더하기만하는 방식은 10 10 10 10과 같은 테스트 케이스에서 최소 비교 횟수를 확보하지 못함
# 메모 2 : 왜? 순차적으로 더하기만 하면 누적된 값을 합할 때 오름차순 순서가 유지되지 않음
# 메모 3 : 왜 이 부분을 놓쳤을까 ? 문제에서 카드묶음의 개수가 동일할 수도 있다는 사실을 인식하지 못함

# ----------------------
# <두 번째 시도 - 시간 초과>

# N = int(input())
# arr = []

# for _ in range(N):
#   arr.append(int(input()))

# total = 0

# while len(arr) >= 2:
#   arr.sort()
#   sum = arr[0] + arr[1]
#   total += sum
#   arr.append(sum)
#   arr = arr[2:]

# print(total)

# 메모 4 : 해결 방법(매번 오름차순 정렬하면서 가장 작은 두 수를 뽑아 연산)으로 구현했을 때 시간 초과 발생
# 메모 5 : 왜 ? 입력의 개수가 많아질 수록 매번 정렬을 수행하고 그 정렬 한 번의 수행 시간도 길어져 시간 복잡도가 너무 높아짐
# 메모 6 : 그렇다면 오름차순 정렬을 빠르게 하는 방법이 있을까? 힙정렬(최소, 최대값을 빠르게 찾아내기 위한 완전 이진 트리를 기반으로 하는 트리)을 이용하고 파이썬에서 제공하고 있는 heap 모듈 활용
# 메모 7 : python으로는 모듈을 써서 구현하면 되지만 주력 언어인 javascript로도 가능할까? 힙정렬 관련 깊이 있는 이해 후 시도해보기

# ----------------------
# <세 번째 시도 - 성공>
from heapq import heappush, heappop

N = int(input())
cards = []

for _ in range(N):
  heappush(cards, int(input()))

total = 0

while len(cards) >= 2:
  sum = heappop(cards) + heappop(cards)
  heappush(cards, sum)
  total += sum

print(total)
