T = int(input())

for _ in range(T):
	N = int(input())
	if N == 0 or N == 1:
		print(1)
	elif N < 3:
		print(N)
	elif N == 3:
		print(6)
	elif N == 4:
		print(4)
	else:
		print(0)
