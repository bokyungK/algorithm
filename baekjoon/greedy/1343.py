# 폴리오미노

board = input().split('.');

for idx, item in enumerate(board):
  length = len(item)
  a_string = 'AAAA' * (length // 4)
  b_string = 'BB' * ((length % 4) // 2)

  if (length % 2 == 1):
    print(-1)
    break

  board[idx] = a_string + b_string

else:
  print('.'.join(board))

# 파이썬의 for문과 else문을 결합해서 사용하면 반복문을 끝까지 정상적으로 완수한 후에만 else문을 실행하기 때문에 유용하다.
# 4와 2길이의 조합이기 때문에 부분 문자열의 길이가 하나라도 홀수면 -1을 출력한다. 굳이 남아있는 X를 다시 찾는 과정은 복잡도를 높인다.
