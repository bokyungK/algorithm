# 단어 수학

N = int(input())
alphabet_dict = {}
text_list = [input() for _ in range(N)]
sum = 0
cnt = 9

for text in text_list:
  length = len(text)
  for i, char in enumerate(text):
    digits = 10 ** (length - i - 1)
    alphabet_dict[char] = alphabet_dict.get(char, 0) + digits

for digits in sorted(alphabet_dict.values(), reverse=True):
  sum += digits * cnt
  cnt -= 1

print(sum)