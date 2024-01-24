m = int(input())
n = int(input())

proportion = 0
empty = 0

for _ in range(n):
    for i in str(input()):
        if i == ".":
            empty += 1

proportion = empty / (m * n)

print(proportion)
