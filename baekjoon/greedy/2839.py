# 설탕 배달
sugar = int(input())

fiveCnt = sugar // 5
result = -1

while fiveCnt > -1:
    threeCnt = (sugar - (5 * fiveCnt)) // 3

    if 5 * fiveCnt + 3 * threeCnt == sugar:
        result = fiveCnt + threeCnt
        break
    else:
        fiveCnt -= 1

print(result)
