# 게임을 만든 동준이

n = int(input())
score_list = [int(input()) for _ in range(n)]
prev_score = score_list[-1]
answer = 0

for score in reversed(score_list[:-1]):
  if score >= prev_score:
    answer += score - prev_score + 1
    prev_score -= 1
  else:
    prev_score = score

print(answer)

# 요구사항의 범위를 제대로 확인하고 최소, 최대값 변수의 초기 값을 할당하기
  # 1 <= score < 20000이므로 score를 999로 초기화해서는 안된다.
# 변수의 이전 값과 연산해서 갱신하는 경우와, 새로운 값을 할당하는 경우를 명확히 구분하면서 작성하기
# 리팩토링
  # 점수가 항상 높다는 보장이 없기 때문에 higher_score 보다 prev_score가 더 명확한 변수명이다.
  # 반복문에서 첫 번째 순회는 항상 거짓으로 정해져있으므로 굳이 시행하지 않도록 반복문 범위를 슬라이싱
  # diff 변수를 사용할 필요 없이 answer에서만 점수의 차이를 계산하고, prev_score는 항상 이전 값보다 1만 작게 만들면 되기 때문에 -1 연산을 해준다.