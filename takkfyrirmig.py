n = int(input())
guests = []

for _ in range(n):
	name = str(input())
	guests.append(name)

for i in range(len(guests)):
	print("Takk " + guests[i])
