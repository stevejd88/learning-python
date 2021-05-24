# arranged_problems = "Hello\nWorld"
arranged_problems = []
problemsdict = {}


def arithmetic_arranger(problems):
  count = 0
  for problem in problems:
    obj = dict()
    item = problem.split(" ")
    obj['top'] = item[0]
    obj['operator'] = item[1]
    obj['bottom'] = item[2]

    dashes = []
    daschCount = 0
    if len(item[0]) > len(item[2]):
      dashCount = len(item[0]) + 2
    elif len(item[2]) > len(item[0]):
      dashCount = len(item[2]) + 2
    elif len(item[2]) == len(item[0]):
      dashCount = len(item[2]) + 2

    while dashCount > 0:
      dashes.append("-")
      dashCount = dashCount - 1

    obj['dash'] = "".join(dashes)
    problemsdict[f"obj{count}"] = obj
    count = count + 1

    

  print(problemsdict)

arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"])

for x in problemsdict:
  if len(problemsdict[x]["top"]) >= len(problemsdict[x]["bottom"]):
    arranged_problems.append("  ")
  elif len(problemsdict[x]["top"]) < len(problemsdict[x]["bottom"]):
    space = len(problemsdict[x]["bottom"]) - len(problemsdict[x]["top"]) + 2
    while space > 0:
      arranged_problems.append(" ")
      space = space - 1
  arranged_problems.append(problemsdict[x]["top"])
  arranged_problems.append("    ")

arranged_problems.append("\n")

for y in problemsdict:
  space = 0
  arranged_problems.append(problemsdict[y]["operator"])

  if len(problemsdict[y]["top"]) > len(problemsdict[y]["bottom"]):
    space = len(problemsdict[y]["top"]) - len(problemsdict[y]["bottom"]) + 1
  
  else: 
    space = 1

  while space > 0 :
      arranged_problems.append(" ")
      space = space - 1

  arranged_problems.append(problemsdict[y]["bottom"])
  arranged_problems.append("    ")

arranged_problems.append("\n")

for z in problemsdict:
  arranged_problems.append(problemsdict[z]["dash"])
  arranged_problems.append("    ")


print("".join(arranged_problems))