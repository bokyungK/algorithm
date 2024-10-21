# 뒤집기
S = input()
prevTxt = -1
zeroCnt = 0
oneCnt = 0

for txt in S:
  if txt != prevTxt :
    if (txt == '0'):
      zeroCnt += 1
    else:
      oneCnt += 1

  prevTxt = txt

print(zeroCnt if zeroCnt <= oneCnt else oneCnt)

# 해결 방법 : 포인트는 문자가 바뀌는 순간이 아니라 문자의 덩어리가 몇 개인지 세는 것!