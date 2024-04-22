import math

n = int(input())

days = math.ceil(math.log(n) / math.log(2)) + 1

print(days)
