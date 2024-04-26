n = int(input())
working = True

for _ in range(3):
	if "7" not in input().split():
		working = False

print(777 if working else 0)
