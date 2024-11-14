# 한 줄로 서기

N = int(input())
taller_list = list(map(int, input().split()))
answer = [0] * N

for i, taller_cnt in enumerate(taller_list):
  zero_cnt = 0

  for j in range(N):
    if answer[j] == 0:
      if zero_cnt == taller_cnt:
        answer[j] = i + 1
        break
      
      zero_cnt += 1

print(' '.join(map(str, answer)))

# 규칙이 전체 원소에 다 해당되는지 테스트 후 코드 짜기
# zero_cnt와 taller_cnt가 같을 때 바로 값을 할당하면, 이미 값이 저장되어 있는 값에 덮어씌워지는 문제가 있음
# 해당 위치의 값이 0인지 아닌지 먼저 체크가 필요 (0이 아니면 다음 위치로 이동)
# 파이썬은 js와 다르게 타입에 엄격하다.
  # join을 할 때 배열 안에 원소가 문자열로 이루어져 있어야 한다.
  # 문자열의 특정 인덱스의 값만 재할당할 수 없다. (ex) txt[0] = '1'