# 5와 6의 차이

A, B = input().split()
min_sum = int(A.replace('6', '5')) + int(B.replace('6', '5'))
max_sum = int(A.replace('5', '6')) + int(B.replace('5', '6'))

print(min_sum, max_sum)

# min, max와 같은 예약어 사용에 주의하기
