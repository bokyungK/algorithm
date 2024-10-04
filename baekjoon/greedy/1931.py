# 회의실 배정

# 입력
meetings = int(input())
timeList = []

for _ in range(meetings):
  time = list(map(int, input().split()))
  timeList.append(time)

# 출력
timeList.sort(key=lambda x: (x[1], x[0]))
prevEnd = 0
maxMeetCnt = 0

for start, end in timeList:
  if (prevEnd <= start):
    maxMeetCnt += 1
    prevEnd = end

print(maxMeetCnt)

# 메모 : 회의를 최대한 많이 하려면 이전 회의가 시작하는 시간보다 끝나는 시간이 중요
# 메모2 : 초기화 값이 loop 첫 수행문과 겹치지 않는지 체크