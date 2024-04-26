n = int(input())
highest = ["", 0]

for _ in range(n):
	gift = str(input()).split()
	if int(gift[1]) > int(highest[1]):
		highest[0] = gift[0]
		highest[1] = gift[1]

print(highest[0])
