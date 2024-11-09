idx = 1

while True:
  L, P, V = map(int, input().split())

  if L == P == V == 0:
    break
  else:
    answer = L * (V // P) + min(L, (V % P))
    print(f'Case {idx}: {answer}')
    idx += 1