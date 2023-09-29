piecesNeeded = [1, 1, 2, 2, 2, 8]
currentPieces = list(map(int, input().split()))
differences = ""

for i in range(len(piecesNeeded)):
    differences += str(piecesNeeded[i] - currentPieces[i]) + " "

print(differences)
