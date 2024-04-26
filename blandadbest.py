n = int(input())
meats = []

for _ in range(n):
	meat = str(input())
	meats.append(meat)

if n == 1:
	print(meats[0])
else:
	print("blandad best")
