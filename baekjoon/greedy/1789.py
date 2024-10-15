# 수들의 합
S = int(input())
N = 1
sum = 1

while S >= sum:
    N += 1
    sum = N * (N+1) // 2

print(N-1)

# 메모 : 발견한 규칙에서 핵심은 'N까지의 합과 입력받은 숫자의 비교'!
# 메모 2 : 핵심만 파악하면 불필요한 변수 및 로직 X (용도에 맞는 적절한 함수를 사용 할 수 있게 됨)
# 메모 3 : 초기화 값을 갱신할 때 참조되는 값이 먼저 처리되도록 순서 주의!
# 메모 4 : 변수는 로직이 아닌 값을 담는다. 함수와 헷갈리지 말기!