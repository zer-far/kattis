A, B = map(str, input().split())

A, B = A [::-1], B [::-1]

if int(A) > int(B):
	print(A)
else:
	print(B)
