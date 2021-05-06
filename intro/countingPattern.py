counts = dict()
print('Enter a line of text: ')
line = input('')

words = line.split()

print('Words:', words)

print('Counting...')
for word in words:
  counts[word] = counts.get(word,0) + 1
print('Counts', counts)


#  looping through the keys in a dictionary
counts = {'chuck': 1, 'fred' : 42, 'jan': '100'}
for key in counts:
  print(key, counts[key])

print(counts.keys())
print(counts.values())
print(counts.items())

# two iteration variables, loops trhough key-value pairs in a dictionary
for key,value in counts.items() :
  print(key, value)