# 로프
N = int(input())
ropes = []
maxKg = 0

for _ in range(N):
  ropes.append(int(input()))

ropes.sort()

for kg in ropes:
  if (kg * N > maxKg):
    maxKg = kg * N
  N -= 1

print(maxKg)