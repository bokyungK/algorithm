# ATM
person = int(input())
times = list(map(int, input().split()))

total = 0
preTotalTime = 0
times.sort()

# '바로 직전 소요 시간 + 본인 소요 시간' 모두 합하여 출력
for time in times:
  preTotalTime += time
  total += preTotalTime

print(total)