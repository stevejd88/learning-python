data = 'From steven@hello.how.are.you Sat Jan dsjflksjfslf'

# find sarting position to extract
atpos = data.find('@')

# find end position for extraction, looking for first blank ' ' space after starting position
spos = data.find(' ', atpos)

# slice from after @ and up to but not including end position spos
host = data[atpos+1 : spos]
print(host)