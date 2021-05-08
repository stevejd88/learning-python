d = {'a':10, 'b':1, 'c':22}
print(d.items())

# built in sorted function takes a sequence as a paramater and returns a sorted sequence
print(sorted(d.items()))

# =============================================================
c = { 'a':10, 'b':1, 'c':22}
tmp = list()

for k, v in c.items() :
  tmp.append( (v,k) ) 

print(tmp)

tmp = sorted(tmp, reverse=True)
print(tmp)