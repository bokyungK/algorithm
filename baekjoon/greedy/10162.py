# 전자레인지
T = int(input())
buttonTimeList = [300, 60, 10]
result = ''

for time in buttonTimeList:
    result += str(T // time) + ' ' 
    T = T % time
 
if T != 0: result = -1
print(result)

# 메모 : python은 서로 다른 타입간의 연산 불가능 (print의 sep=' '를 사용할 때 string + int 에러 주의)