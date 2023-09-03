N = int(input())
integers = list(map(int, input().split()))
total = 0

for i in range(N):
	total += integers[i]

print(total)
