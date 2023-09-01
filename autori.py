long_variation = str(input())
short_variation = ""

for i in range(len(long_variation)):
	if long_variation[i].isupper():
		short_variation += long_variation[i]

print(short_variation)
