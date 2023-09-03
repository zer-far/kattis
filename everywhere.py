T = int(input())

for _ in range(T):
	n = int(input())
	cities = set()

	for i in range(n):
		cities.add(str(input()))

	print(len(cities))
