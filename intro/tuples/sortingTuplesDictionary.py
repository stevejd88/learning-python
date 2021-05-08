fhand = open('../words.txt')
counts = dict()
for line in fhand:
  words = line.split()
  for word in words:
    counts[word] = counts.get(word, 0) + 1

print(counts)

lst = list()
for key, val in counts.items():
  newtup = (val, key)
  lst.append(newtup)

lst = sorted(lst, reverse=True)

for val, key in lst[:10] :
  print(key, val)


# creates a osrt of tuples for eac item in c.items()
print(sorted( [ (v,k) for k,v in counts.items() ]))