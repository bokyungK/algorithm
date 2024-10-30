# 강의실 배정
import heapq
import sys

input = sys.stdin.readline
N = int(input())
room_list = [list(map(int, input().split())) for _ in range(N)]
heap = []

room_list.sort(key=lambda x: (x[0], x[1]))

for start, end in room_list:
    if heap and heap[0] <= start:
        heapq.heappop(heap)
    heapq.heappush(heap, end)

print(len(heap))