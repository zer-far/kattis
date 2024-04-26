s = str(input()).lower()
vowels = "aeiou"
count = 0
countY = 0

for i in range(len(s)):
	for j in range(len(vowels)):
		if s[i] == vowels[j]:
			count += 1
	if s[i] == "y":
		countY += 1

print(count, countY + count)
