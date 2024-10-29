# 수 묶기
import heapq

N = int(input())
positive_heap = []
negative_heap = []
zero_cnt = 0
one_cnt = 0

# 입력
for _ in range(N):
  num = int(input())
  if num > 1:
    heapq.heappush(positive_heap, -num)
  elif num < 0:
    heapq.heappush(negative_heap, num)
  elif num == 1:
    one_cnt += 1
  else:
    zero_cnt += 1

# 출력
def getSum(heap, is_positive):
  global zero_cnt
  total = 0

  while heap:
    sign = -1 if is_positive else 1
    num1 = sign * heapq.heappop(heap)
    num2 = sign * heapq.heappop(heap) if heap else 1

    if not is_positive and zero_cnt > 0 and num2 == 1:
      num2 = 0
      zero_cnt -= 1
      
    total += num1 * num2

  return total

print(getSum(positive_heap, True) + getSum(negative_heap, False) + one_cnt)
# 오름차순으로 정렬한 음수 배열에서 두개씩 묶고 남은 수는 0이 있으면 곱해주거나 없으면 합산 처리