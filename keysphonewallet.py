N = int(input())
itemsNeeded = ["keys", "phone", "wallet"]
items = []
forgot = []

for _ in range(N):
	items.append(str(input()))

for i in range(len(itemsNeeded)):
	if itemsNeeded[i] not in items:
		forgot.append(itemsNeeded[i])

if len(forgot) == 0:
	print("ready")
else:
	for i in forgot:
		print(i)
