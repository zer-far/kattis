name = str(input())
compactName = ""
last = ""

for i in range(len(name)):
    if last != name[i]:
        compactName += name[i]
    last = name[i]

print(compactName)
