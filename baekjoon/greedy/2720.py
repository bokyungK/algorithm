# 세탁소 사장 동혁
case = int(input())
unitList = [25, 10, 5, 1]

for _ in range(case):
  change = int(input())

  for unit in unitList:
    print(change // unit, end=' ')
    change = int(change % unit)
  print()

  # 메모 : (line 11) print는 기본으로 end='\n'을 추가. 따라서 print('\n')은 줄바꿈 출력 후 end='\n' 한 번 더 수행.
  # 메모2 : sep은 여러 값을 쉼표로 구분해서 '한 번에 출력'할 때, end는 print가 실행된 후 '출력의 끝'에 추가