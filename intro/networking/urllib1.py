import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in fhand:
  # print(line.decode().strip())
  words = line.decode().split()
  for word in words:
    counts[word] = counts.get(word, 0) + 1
print(counts)



# READING A WEBPAGE
lhand = urllib.request.urlopen('http://www.dr-chuck.com/page1/htm')
for line in lhand:
  print(line.decode().strip())