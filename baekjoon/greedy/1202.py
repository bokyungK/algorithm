# 보석 도둑

import heapq
import sys

input = sys.stdin.readline
N, K = map(int, input().split())
gems = [list(map(int, input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]
gems.sort()
bags.sort()

heap = []
j = 0
answer = 0

for i in range(K):
  while j < len(gems) and gems[j][0] <= bags[i]:
    heapq.heappush(heap, -gems[j][1])
    j += 1
      
  if heap:
    answer += -heapq.heappop(heap)
      
print(answer)

# 가격을 내림차순으로 정렬하고 그 중 가장 큰 보석부터 찾으면, 보석 크기가 뒤죽박죽이 돼서 모든 경우를 매번 순회하느라 복잡도가 너무 커짐
# 오름차순으로 정렬 후 더 경우의 수가 적은 작은 보석부터 확인하면서 현재 가방에 담을 수 있는 보석 중 가장 큰 가격만 합산하면 복잡도 개선할 수 있음
# 최소, 최대값을 빠르게 찾으려면 우선순위 큐(heap 큐) 알고리즘을 이용