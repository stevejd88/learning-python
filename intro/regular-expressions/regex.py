import re

hand = open('../words.txt')
for line in hand:
  line = line.rstrip()
  if re.search('^The', line) :
    print(line)

x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+',x)
print(y)