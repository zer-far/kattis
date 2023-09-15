n, x = map(int, input().split())
bottlesNeeded = 0

for _ in range(n):
    bottlesNeeded += int(input())

if x >= bottlesNeeded:
    print("Jebb")
else:
    print("Neibb")
