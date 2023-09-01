N, W, H = map(int, input().split())
length = ((W ** 2) + (H ** 2)) ** 0.5

for _ in range(N):
	if int(input()) <= length:
		print("DA")
	else:
		print("NE")
