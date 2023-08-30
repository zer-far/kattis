text = str(input())
length = len(text)
whitespace_count = 0
lowercase_count = 0
uppercase_count = 0
symbol_count = 0

for i in range(length):
	if text[i] == "_":
		whitespace_count += 1
	elif text[i].islower():
		lowercase_count += 1
	elif text[i].isupper():
		uppercase_count += 1
	else:
		symbol_count += 1

whitespace_ratio = whitespace_count/length
lowercase_ratio = lowercase_count/length
uppercase_ratio = uppercase_count/length
symbol_ratio = symbol_count/length

print(whitespace_ratio)
print(lowercase_ratio)
print(uppercase_ratio)
print(symbol_ratio)
