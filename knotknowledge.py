n = int(input())
knots = set(input().split())
knotsLearned = set(input().split())

print(knots.difference(knotsLearned).pop())
