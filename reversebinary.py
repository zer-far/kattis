N = int(input())

reversedN = int(str(bin(N)).replace("0b", "")[::-1], 2)

print(reversedN)
