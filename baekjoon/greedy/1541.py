# 잃어버린 괄호
formula = input()
minusIdx = formula.find('-')

def getSum(string):
    return sum(list(map(int, string.split('+'))))

if minusIdx < 0:
    print(getSum(formula))
else:
    left = formula[:minusIdx]
    right = formula[minusIdx + 1:].replace('-', '+')
    print(getSum(left) - getSum(right))