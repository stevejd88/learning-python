import re
lin = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'

# [^ ] means starting with non-blank character, and will keep going until you hit a blank
y = re.findall('@([^ ]*)', lin)

# More precise, because we specify to ^start at From
y = re.findall('^From .*@([^ ]*)', lin)
print(y)

x = 'We just received $10.00 for cookies.'
# Back slash \ is an escape to signigy that the character that follows is a real symbol. Here
# it is a dollar sign
y = re.findall('\$[0-9.]+', x)
print(y)