message = str(input())
author = ""
smiley_count = message.count(":)")
frowny_count = message.count(":(")

if smiley_count > 0 and frowny_count == 0:
	author = "alive"
elif smiley_count == 0 and frowny_count > 0:
	author = "undead"
elif smiley_count > 0 and frowny_count > 0:
	author = "double agent"
else:
	author = "machine"

print(author)
