# 팰린드롬 만들기

en_name = list(input())
en_length = len(en_name)
dict_s = {}

for s in en_name:
  dict_s[s] = dict_s.get(s, 0) + 1

odd_part = ''
even_part = ''
answer = "I'm Sorry Hansoo"

for key in sorted(dict_s.keys()):
  count = dict_s[key]
  even_part += key * (count // 2)

  if count % 2 == 1:
    odd_part += key

if (en_length % 2 == 0 and len(odd_part) == 0) or (en_length % 2 == 1 and len(odd_part) == 1):
    answer = even_part + odd_part + even_part[::-1]

print(answer)