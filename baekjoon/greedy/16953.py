# A -> B

start, end = map(int, input().split(' '))
cnt = 1

while start < end:
  if end % 10 == 1:
    end = end // 10
  elif end % 2 == 0:
    end = end // 2
  else:
    break

  cnt += 1

print(cnt if start == end else -1)

# 생각한 해결 방법 : start -> end로 찾아나갈땐 경우의 수가 두 가지, end -> start는 마지막 자리수 기준으로 경우의 수를 한 가지로 좁힐 수 있음
# 리팩토링
# 1) 짝수는 일의 자리만 추출하지 않아도 원래 수를 나눴을 때 0이니까 일의 자리 변수를 굳이 만들지 않는게 가독성이 더 좋음
# 2) cnt를 최종적으로 + 1을 해야할 때는 마지막 단계에서 할 필요 없이 처음에 1로 초기화 해주면 더 깔끔한 코드 작성 가능
# 3) 마지막에서 else인 경우를 모두 -1로 처리해주기 때문에, while 안에 else(일의 자리가 1이 아닌 홀수인 모든 경우)의 실행문에서 cnt = -1는 불필요한 코드이므로 제거
