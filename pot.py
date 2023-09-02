N = int(input())
X = 0

for _ in range(N):
	num = int(input())
	power = num % 10
	new_num = num // 10
	X += new_num ** power

print(X)
