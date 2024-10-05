# 잃어버린 괄호
formula = input()
minusIdx = formula.find('-')

if minusIdx < 0:
    total = list(map(int, formula.split('+')))
    print(sum(total))
else:
    left = list(map(int, formula[:minusIdx].split('+')))
    right = list(map(int, formula[minusIdx+1:].replace('-', '+').split('+')))
    print(sum(left) - sum(right))