# handle = open(filename, mode)
# filename is a string
# mode, optinal paramater to reade or write "r,w"

fhand = open('login-book.csv')
count = 0

# print each line in the file
for cheese in fhand:
  count = count + 1
  # Delete newline white space
  cheese = cheese.rstrip()

  # skip any lines of the file that do not contain the string, and continue
  if not '2020' in cheese :
    continue
  print(cheese)

print('Line Count:', count)


shand = open('login-book.csv')
inp = shand.read()
print(len(inp))

# print from the 20th chacacter on up
print(inp[:20])