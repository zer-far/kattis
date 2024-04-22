differences = []

while True:
	try:
		a, b = map(int, input().split())
		difference = abs(a - b)
		differences.append(difference)
	except EOFError:
		break
	except ValueError:
		break

for i in range(len(differences)):
	print(differences[i])
