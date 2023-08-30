from math import ceil

A, I = map(float, input().split())

scientists = ceil(A * (I - 1)) + 1

print(scientists)
