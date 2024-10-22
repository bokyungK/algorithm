# 신입 사원
T = int(input())

for _ in range(T):
  N = int(input())
  ranks = [list(map(int, input().split())) for _ in range(N)]
  ranks.sort()
  
  answer = 1
  minRank = ranks[0][1]

  for rank in ranks:
    interviewRank = rank[1]

    if interviewRank < minRank:
      answer += 1
      minRank = interviewRank

  print(answer)

# 문제의 요구사항대로 직접 비교해서 제대로 핵심 파악하기 => 비교해서 하나가 높기만 하면 되는 것이 아니라, '둘중에 하나가' 높아야 한다.
# 사용한 값은 다음 반복문 수행 전에 초기화 필수
# 요구사항 값의 범위 꼭 체크
# 입력 자체에서 시간이 많이 소요되는 경우 sys.stdin.readline() 사용 또는 pypy3로 제출
# 2차원 배열 만들 때 더 간략하게 작성하는 방법 숙지