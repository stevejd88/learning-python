counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']

#  exactly the same as code down below,using the get method we pass in a key value to look up,
# 'name' and the second argument is the default value if no key is found
for name in names :
  counts[name] = counts.get(name,0) + 1
print(counts)

# for name in names : 
#   if name not in counts:
#     counts[name] = 1
#   else :
#     counts[name] = counts[name] + 1
# print(counts)