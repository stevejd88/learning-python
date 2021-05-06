d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k,v) in d.items():
  print(k,v)

tups = d.items()
print(tups)

# tuples are comparable
# if first item is equal, python goes on to the next element until it finds elements that differ
print((0,1,2) < (5,1,2))