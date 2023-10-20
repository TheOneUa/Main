import sys
import math
from collections import Counter
alphabet='abcdefghijklmnopqrstuvwxyz'
alphabet2='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

result = []
text = input.replace(' ', '').replace('e','').lower()
ind = 0
# Count the frequency of each character
character_count = Counter(text)
# Get the most common letter and its count
most_common_letter = character_count.most_common(1)[0][0]
most_common_letter_count = character_count.most_common(1)[0][1]
#самая употребляемая буква
print(character_count)
print(most_common_letter)
print(most_common_letter_count)


#находим сдвиг
for i in range (len(alphabet)):
  if alphabet[i] == most_common_letter[0]:
    i = 4 - i
    shift = i
    print('shift = ', shift)
    break

#decode shift:
for a in range(len(input)):
#  if input[a] == str.isupper(input[a]):
  if input[a].lower() not in alphabet:
    res = input[a]
  else:
    if input[a] in alphabet2:
      symbol = input[a]
 #     print('symbol = ',symbol)
      index = int(alphabet2.find(symbol)) + shift
 #     print('index shifted = ',index)
      if index > 25:
         index = index % 26
      if index < 0:
         index = index % 26

    res = alphabet2[index]
    index = 0
   # print('res = ', res)
    if input[a] in alphabet:  
      symbol = input[a].lower()
  #    print('symbol = ',symbol)
      index = int(alphabet.find(symbol)) + shift
 #     print('index shifted = ',index)
      if index > 25:
        index = index % 26
      if index < 0:
          index = index % 26
    
      res = alphabet[index]
      index = 0
#      print('res = ', res)
  result.append(res)
print(''.join(result))