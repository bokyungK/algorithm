N = input()
max = -1

if '0' in N:
  arr = list(N)

  digitSum = sum(map(int, N))

  if digitSum % 3 == 0:
    max = ''.join(sorted(N, reverse=True))

print(max)

# 순열을 하나하나 찾는 작업은 입력의 길이가 길어지면 시간 초과 발생
# 30의 배수의 일의 자리 값은 0으로 끝나기만 하지 않고, 모든 자리 수의 합이 3의 배수일 때 참이라는 규칙성을 찾아야 됨