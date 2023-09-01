n = int(input())
temperatures = list(map(int, input().split()))
subzero = 0

for i in range(n):
	if temperatures[i] < 0:
		subzero += 1

print(subzero)
