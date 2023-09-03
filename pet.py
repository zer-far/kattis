points = []

for i in range(5):
	points.append(sum(map(int, input().split())))

winner_points = max(points)
winner = points.index(winner_points) + 1

print(winner, winner_points)
