# 행렬

n, m = map(int, input().split())
matrix_a = [list(input()) for _ in range(n)]
matrix_b = [list(input()) for _ in range(n)]
answer = 0

for i in range(n - 2):
  for j in range(m - 2):
    if matrix_a[i][j] != matrix_b[i][j]:
      for k in range(3):
        matrix_a[i+k][j] = '1' if matrix_a[i+k][j] == '0' else '0'
        matrix_a[i+k][j+1] = '1' if matrix_a[i+k][j+1] == '0' else '0'
        matrix_a[i+k][j+2] = '1' if matrix_a[i+k][j+2] == '0' else '0'
      answer += 1

print(answer if matrix_a == matrix_b else -1)

# 문제를 완전히 이해하고 풀어야 시간을 아낄 수 있다.
# 3x3 크기의 부분 행렬의 원소를 모두 뒤집는 것이 포인트
# 원소 하나씩 순회하며 비교 후 다르면 뒤집는다. 이미 뒤집은 원소는 b 행렬과 맞춰놓았기 때문에 신경쓰지 않아도 된다. (현위치를 기준으로 idx가 높은 위치만 3x3만큼 체크)
# 입력으로 받아오는 문자열 값을 제어할 때 숫자형과 충돌이 나지 않도록 유의


