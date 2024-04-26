P = int(input())
candles = []

for _ in range(P):
	K, N = map(int, input().split())
	candlesNeeded = 0

	for i in range(N + 1):
		candlesNeeded += i + 1

	candlesNeeded -= 1

	candles.append(candlesNeeded)

for i in range(P):
	print(i + 1, candles[i])
