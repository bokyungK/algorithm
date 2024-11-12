# 수리공 항승

N, L = map(int, input().split())
water_area = list(map(int, input().split()))
prev_area = -999
extra_len = L - 1
answer = 0

for cur_area in sorted(water_area):
  if cur_area - prev_area <= extra_len:
    extra_len -= cur_area - prev_area
  else:
    answer += 1
    extra_len = L - 1

  prev_area = cur_area

print(answer)

# 좌우 0.5씩 총 1의 길이는 기본으로 필요하기 때문에 '테이프 길이 - 1' 값과 물이 새는 위치의 차이 값을 비교