n, k = map(int, input().split())
remaining_voters = n - k
ratings = 0

for _ in range(k):
	ratings += int(input())

minimum_overall_rating = (ratings + (-3 * remaining_voters)) / n
maximum_overall_rating = (ratings + (3 * remaining_voters)) / n

print(minimum_overall_rating, maximum_overall_rating)
