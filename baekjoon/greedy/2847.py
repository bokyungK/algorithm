# 게임을 만든 동준이

n = int(input())
score_list = [int(input()) for _ in range(n)]
higher_score = float("inf")
answer = 0

for score in reversed(score_list):
  if score >= higher_score:
    diff = (score - higher_score + 1)
    higher_score = score - diff
    answer += diff
  else:
    higher_score = score

print(answer)

# 요구사항의 범위를 제대로 확인하고 최소, 최대값 변수의 초기 값을 할당하기
# 1 <= score < 20000이므로 score를 999로 초기화해서는 안된다.
