friends = ['Andrea', 'Lilu','Lola']

for i in range(len(friends)) :
  friend = friends[i]
  print('Happy New Year:', i, friend)

a = [1,2,3]
b = [4,5,6]

c = a + b
print(c)

# slice c from index to up to but not including index 4
print(c[2:4])

# check for something in a list
# call also check "not in"
print(7 in c)

# built in sum method to lists
print(sum(c) / len(c))

numlist = list()
count = 0
while True :
  inp = input('Enter a number: ')
  if inp == 'done' : break
  value = float(inp)
  numlist.append(value)

average = sum(numlist) / len(numlist)
print('Average:', average)