fees = []

for _ in range(3):
    fees.append(int(input()))

minIndex = fees.index(min(fees))

if minIndex == 0:
    print("Monnei")
elif minIndex == 1:
    print("Fjee")
else:
    print("Dolladollabilljoll")
