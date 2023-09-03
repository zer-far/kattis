grades = []

for i in range(5):
	grades.append(sum(map(int, input().split())))

points = max(grades)
winner = grades.index(points) + 1

print(winner, points)
