# 저울

n = input()
arr = list(map(int, input().split()))
target = 1

for weight in sorted(arr):
  if target < weight:
    break

  target += weight 

print(target)

# 각 무게를 오름차순으로 정렬하고 순차적으로 무게추를 더했을 때 끊어지는 구간을 찾기